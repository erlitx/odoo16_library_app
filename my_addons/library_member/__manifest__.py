# -*- coding: utf-8 -*-
{
    'name': "Library Member",

    'summary': """
        Add a custom field to library_app """,

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
    'depends': ['library_app', 'mail'],
    'data': ["security/ir.model.access.csv", "views/book_view.xml", "views/library_menu.xml", "views/member_view.xml",],
    # only loaded in demonstration mode
    'demo': ["data/res.partner.csv", "data/library.book.csv", "data/book_demo.xml"],
    'application': False
}
