# -*- coding: utf-8 -*-

{
    'name': "Odoo Academy",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_management'],

    # always loaded
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_view.xml',
        'views/sale_views_inherit.xml',
        'views/product_views.xml',
        'wizard/sale_wizard_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/academy_demo.xml'
    ],
    
    'license': 'GPL-2'
}