# -*- coding: utf-8 -*-

from odoo import api, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    @api.multi
    def capture_image(self):
        return {
            'name': 'Capture Image',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'wiz.capture.pic',
            'type': 'ir.actions.act_window',
            'target': 'new',
        }
