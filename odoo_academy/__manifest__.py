{
    'name': 'Odoo Academy ADN',
    'summary': """Academy app to manage training""",
    'description': """
        Academy module to manage training
    """,
    'author': 'El Adan',
    'website': 'erp.appskurigage.com',
    'category': 'Training',
    'version': '0.1',
    'depends': ['sale_management'],
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/sale_views_inherit.xml',
        'views/product_views_inherit.xml',
        'wizard/sale_wizard_view.xml',
    ],
    'demo':[
        'demo/academy_demo.xml'
    ],
    'license': 'LGPL-3'
}