# -*- coding: utf-8 -*-
# Part of Swerp. See LICENSE file for full copyright and licensing details.

from swerp import fields, models

class Company(models.Model):
    _inherit = "res.company"

    snailmail_color = fields.Boolean(string='Color', default=False)
    snailmail_duplex = fields.Boolean(string='Both sides', default=False)
