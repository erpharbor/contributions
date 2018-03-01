# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class HrWebCamera(http.Controller):

    @http.route('/hr_web_camera/capture', type='http', method='POST',
                auth='user', csrf=False)
    def capture_image(self, **kw):
        if kw.get('employee_id') and kw.get('file_data'):
            # Upload image in Employee record
            employee_id = int(kw.get('employee_id'))
            request.env['hr.employee'].browse(employee_id).write({
                'image': kw.get('file_data').encode("utf-8").split(',')[1],
            })
