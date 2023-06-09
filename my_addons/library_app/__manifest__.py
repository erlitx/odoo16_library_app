# -*- coding: utf-8 -*-
{
    'name': "Library Management",

    'summary': """
        Manage library catalog""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'license': 'AGPL-3',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services/Library',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product',],

    # always loaded
    'data': ["security/library_security.xml", "security/ir.model.access.csv",
             "views/library_menu.xml", "views/book_view.xml", "views/book_list_template.xml",
             "reports/library_book_report.xml",],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True
}
