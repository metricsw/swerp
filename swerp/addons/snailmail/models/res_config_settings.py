# -*- coding: utf-8 -*-	
# Part of Swerp. See LICENSE file for full copyright and licensing details.

from swerp import fields, models


class ResConfigSettings(models.TransientModel):	
    _inherit = 'res.config.settings'	

    snailmail_color = fields.Boolean(string='Print In Color', related='company_id.snailmail_color', readonly=False)
    snailmail_duplex = fields.Boolean(string='Print Both sides', related='company_id.snailmail_duplex', readonly=False)
