# -*- coding: utf-8 -*-
{
    'name': 'QR Code Purchase',
    'category': 'Base',
    'author': 'ERP Harbor Consulting Services',
    'summary': 'Generate QR Code for Purchase',
    'website': 'www.erpharbor.com',
    'version': '10.0.1.0.0',
    'description': """""",
    'depends': [
        'purchase','ehcs_qr_code_base',
    ],
    'data': [
        'report/purchase_order_report_template.xml',
        'views/qr_code_purchase_view.xml',
    ],
}
