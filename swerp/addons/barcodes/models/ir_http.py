# -*- coding: utf-8 -*-
# Part of Swerp. See LICENSE file for full copyright and licensing details.

from swerp import models


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        res = super(IrHttp, self).session_info()
        res['max_time_between_keys_in_ms'] = int(
            self.env['ir.config_parameter'].sudo().get_param('barcode.max_time_between_keys_in_ms', default='55'))
        return res
