# -*- coding: utf-8 -*-
{
    'name': 'QR Code Purchase',
    'version': '13.0.1.0.0',
    'category': 'Purchase',
    'author': 'ERP Harbor Consulting Services',
    'summary': 'Generate QR Code for Purchase',
    'website': 'http://www.erpharbor.com',
    'description': """""",
    'depends': [
        'ehcs_qr_code_base',
        'purchase',
    ],
    'data': [
        'report/purchase_order_report_template.xml',
        'views/qr_code_purchase_view.xml',
    ],
    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
}
