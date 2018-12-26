# -*- coding: utf-8 -*-
#################################################################################
#
#   Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#   See LICENSE file for full copyright and licensing details.
#   License URL : <https://store.webkul.com/license.html/>
# 
#################################################################################

from odoo import api, fields, models, _
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
import pytz
import time

class PosSession(models.Model):
    _inherit = "pos.session"

    def _wk_get_utc_time_(self,session_date):
        if session_date:
            try:
                session_date = datetime.strptime(session_date, "%Y-%m-%d %H:%M:%S")
                tz_name = self._context.get('tz') or self.env.user.tz
                tz = tz_name and pytz.timezone(tz_name) or pytz.UTC
                return fields.Datetime.to_string((pytz.UTC.localize(session_date.replace(tzinfo=None), is_dst=False).astimezone(tz).replace(tzinfo=None)))
                
            except ValueError:
                return session_date
    @api.model
    def wk_session_sale_details(self):
        for self_obj in self:
            orders = self_obj.order_ids
            products_sold = {}
            total_sale = 0.0
            order_details = []
            start_date = None
            stop_date = None
            if self_obj.start_at:
                start_date = self_obj._wk_get_utc_time_(self_obj.start_at)
            if self_obj.stop_at:
                stop_date = self_obj._wk_get_utc_time_(self_obj.stop_at)
                 
            for order in orders:
                for line in order.lines:
                    key = (line.product_id)
                    products_sold.setdefault(key, 0.0)
                    products_sold[key] += line.qty
                total_sale += order.amount_total
                wk_order = {
                    'name':order.name,
                    'partner':order.partner_id.name if order.partner_id else '',
                    'date':order.date_order[0:10] if order.date_order else '',
                    'picking':order.picking_id.name if order.picking_id else '',
                    'total_tax':order.amount_tax,
                    'total_amount':order.amount_total,
                    'state':order.state,
                }
                order_details.append(wk_order)
            product_sold_list = sorted(products_sold.items(), key=lambda t: t[1] ,reverse = True)

            return {
                'products': [{
                    'product_id': product.id,
                    'product_name': product.name,
                    'code': product.default_code,
                    'quantity': qty,
                    'uom': product.uom_id.name
                } for (product), qty in product_sold_list],
                'total_sale':total_sale,
                'order_details':order_details,
                'start_date':start_date or '',
                'stop_date':stop_date or ''
            }
    @api.model
    def get_session_report_data(self, kwargs):
        session = self.browse(kwargs['session_id'])
        report_data = session.wk_session_sale_details() or {}
        report_data['session_info'] = {
            'name':session.name,
            'responsible':session.user_id.name,
            'start_date':session._wk_get_utc_time_(session.start_at) or '',
            'opening_balance':session.cash_register_balance_start,
            'total_balance':session.cash_register_total_entry_encoding,
        }
        statement_data = []
        for statement in session.statement_ids:
            statement_details = {
                'name':statement.journal_id.name,
                'balance_start': statement.balance_start,
                'total_trans': statement.total_entry_encoding,
                'balance_end': statement.balance_end_real,
                'difference': statement.difference,
            }
            statement_data.append(statement_details)
        report_data['statements'] = statement_data

        return report_data
         


    @api.multi
    def wk_print_session_report(self):
        return self.env.ref('pos_session_report_all_in_one.action_wk_report_pos_session_summary').report_action(self)

    @api.multi
    def wk_send_sesssion_report(self):
        context = self._context
        template_id = self.env.ref('pos_session_report_all_in_one.pos_session_report_notify_email',False)
        try:
            compose_form = self.env.ref('mail.email_compose_message_wizard_form',False)
        except ValueError:
            compose_form = False 
        if context==None:
            ctx={}
        else:    
            ctx = dict(context)
        ctx.update({
            'default_model': 'pos.session',
            'default_res_id': self.id,
            'default_use_template': bool(template_id),
            'default_template_id': template_id.id,
            })
        return {
            'name': _('Compose Email'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form.id, 'form')],
            'view_id': compose_form.id,
            'target': 'new',
            'context': ctx,
        }