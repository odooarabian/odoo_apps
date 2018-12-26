# -*- coding: utf-8 -*-
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
#################################################################################
{
  "name"                 :  "POS Full Session Report Print",
  "summary"              :  "This module prints POS S Printn ession Summary as well as send Session Summary to the current login user.",
  "category"             :  "Point Of Sale",
  "version"              :  "11.01.01",
  "author"               :  "ERP World",
  "website"              :  "https://www.erpworld.ml"
  "description"          :  """POS Session Report , POS Session Report Analysis, Session Report in Running Session, Session report as receipt
                              POS Sales Report, User Wise Session Summary, Session Summary in Running Session, Print Session Summary, POS Summary,
                              https://www.erpworld.ml
                            """,
"depends"              :  [
                             'point_of_sale',
                             'mail',
                            ],
  "data"                 :  [
                             'views/pos_session_report_view.xml',
                             'views/report_session_summary.xml',
                             'views/pos_session_view.xml',
                             'edi/wk_session_report.xml',
                             'views/template.xml',
                             'views/pos_config_view.xml',
                            ],
  "images"               :  ['static/description/Banner.png'],
  "qweb"                 :  ['static/src/xml/pos_session_report.xml'],

  "application"          :  True,
  "installable"          :  True,
  "auto_install"         :  False,
  "pre_init_hook"        :  "pre_init_check",
}