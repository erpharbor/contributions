# -*- coding: utf-8 -*-
{
    'name': 'QR Code Invoice',
    'category': 'Base',
    'author': 'ERP Harbor Consulting Services',
    'summary': 'Generate QR Code for Invoice',
    'website': 'www.erpharbor.com',
    'version': '10.0.1.0.0',
    'description': """""",
    'depends': [
        'account','ehcs_qr_code_base',
    ],
    'data': [
        'report/account_invoice_report_template.xml',
        'views/qr_code_invoice_view.xml',
    ],
}
