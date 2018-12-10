{
    "name": """POS Kitchen Order Notes By Each Item""",
    "summary": """Set predefined notes for each product or item on kitchen order""",
    "category": "Point of Sale",
    "images": ["images/Banner.png"],
    "version": "11.0.0.0.1",
    "application": False,

    "author": "ERP World",
    "support": "odoo_erp@zoho.com",
    "license": "LGPL-3",
    "price": 20.0,
    "currency": "EUR",

    "depends": [
        "pos_for_restaurant_odoo_base",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "security/ir.model.access.csv",
        "views/views.xml",
        "views/template.xml",
    ],
    "qweb": [
        "static/src/xml/order_note.xml",
    ],
    "demo": [
        "data/pos_product_notes_demo.xml",
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,

    "auto_install": False,
    "installable": True,

    "demo_title": "POS Kitchen Order Notes",
    "demo_addons": [
    ],
    "demo_addons_hidden": [
    ],
    "demo_url": "pos-order-note",
    "demo_summary": "Set predefined notes for each product or item on kitchen order",
    "demo_images": [
        "images/Banner.png",
    ]
}
