# -*- coding: utf-8 -*-
{
    'name': "SNT Rassvet",

    'summary': """
        Application for SNT members collaboration""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'license': 'AGPL-3',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '16.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': ["views/menu_item_snt.xml", "security/ir.model.access.csv", "views/tree_view_meetings_snt_rassvet.xml",
             "views/form_view_meetings_snt_rassvet.xml",],

    # only loaded in demonstration mode
    'demo': [],
    'application': True
}