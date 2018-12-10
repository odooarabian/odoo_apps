{
    "name": """POS restaurants""",
    "summary": """Technical module for POS""",
    "category": "Point of Sale",
    # "live_test_URL": "",
    "images": [],
    "version": "11.0.0.0.1",
    "application": False,

    "author": "ERP World",
    "support": "odoo_erp@zoho.com",
    "license": "LGPL-3",
    "price": 10.0,
    "currency": "EUR",

    "depends": [
        "pos_restaurant",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/template.xml",
    ],
    "qweb": [
    ],
    "demo": [
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,

    "auto_install": False,
    "installable": True,
}
