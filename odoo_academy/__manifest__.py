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
    'depends': ['base'],
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
    ],
    'demo':[
        'demo/academy_demo.xml'
    ],
    'license': 'LGPL-3'
}