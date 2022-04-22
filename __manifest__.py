# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Sales_Discount',
    'version': '1.0',
    'author': 'Muhammad Nasser',
    'summary': 'Sales_Discount',
    'description': """Sales_Discount """,
    'category': 'Productivity',
    'depends': ['sale',
                'product',
                'sales_team',
                ],
    'data': [
        # orders security => data => wizard => views => report
        # menu wizard add in the view files
        'security/security.xml',
        'security/ir.model.access.csv',
        # 'security/ir.model.access.csv',
        # 'data/data.xml',
        # 'wizard/create_appointment_view.xml',
        # 'views/patient_all.xml',
        # 'views/doctor_view.xml',
        # 'views/patient_kids.xml',
        # 'views/appointment_view.xml',
        'views/sale.xml',
        'views/product.xml',
        'views/orders_lines_view.xml',
        # 'report/report_patient_details.xml',
        # 'report/report_appointment_medicine_details.xml',
        # 'report/report.xml',
    ],
    'demo': [],
    'qweb': [],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
