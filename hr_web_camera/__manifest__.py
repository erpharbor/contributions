# -*- coding: utf-8 -*-
{
    'name': "hr_web_camera",
    'version': '10.0.1.0.0',
    'category': 'Human Resources',
    'author': "ERP Harbor Consulting Services",
    'website': "http://www.erpharbor.com",
    'description': """
    This module allow to capture the image of the employee 
    using web camera and upload it on employee record.
    """,
    'depends': [
        'hr',
    ],
    'data': [
        'views/hr_employee_view.xml',
        'views/templates.xml',
        'wizard/wiz_capture_pic_view.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'installable': True,
    'application': True,
}
