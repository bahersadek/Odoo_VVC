# -*- coding: utf-8 -*-
{
    'name': "Vehicles Validation Certificates",

    'summary': """
        licensed by the Ministry of interior to check vehicles and 
        issue validation certificates to them""",

    'description': """
        licensed by the Ministry of interior to check vehicles and 
        issue validation certificates to them
    """,

    'author': "Baher Sadek",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Manufacturing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/vvc_security.xml',
        'security/ir.model.access.csv',
        'views/vvc_traffic_department_view.xml',
        'views/vvc_certificate_type_view.xml',
        'views/vvc_certificates_view.xml',
        'views/vvc_customers.xml',
        'report/vvc_templates.xml',
        'report/vvc_certificate.xml',
    ],
   
}
