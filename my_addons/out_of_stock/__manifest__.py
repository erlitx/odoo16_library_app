# -*- coding: utf-8 -*-
{
    'name': "out_of_stock",

    'summary': """
        This module is used to track products that are not available at a particular location""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/menu_out_of_stock.xml',
        'views/tree_view_out_of_stock.xml',
        'views/tree_view_out_of_stock_custom.xml',
        'security/ir.model.access.csv',
        'views/form_view_out_of_stock.xml',
],
        'application': True,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',

    ],
}
