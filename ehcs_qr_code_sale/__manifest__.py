# -*- coding: utf-8 -*-
{
    'name': 'QR Code Sale',
    'category': 'Base',
    'author': 'ERP Harbor Consulting Services',
    'summary': 'Generate QR Code for Sale',
    'website': 'www.erpharbor.com',
    'version': '10.0.1.0.0',
    'description': """""",
    'depends': [
        'sale','ehcs_qr_code_base',
    ],
    'data': [
        'report/sale_order_report_template.xml',
        'views/qr_code_sale_view.xml',
    ],
}
