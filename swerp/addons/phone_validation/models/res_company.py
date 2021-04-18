# -*- coding: utf-8 -*-
# Part of Swerp. See LICENSE file for full copyright and licensing details.

from swerp import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    phone_international_format = fields.Selection([
        ('no_prefix', 'No prefix'),
        ('prefix', 'Add international prefix'),
    ], string="Local Numbers", default="prefix",
        help="Always encode phone numbers using international format. Otherwise "
             "numbers coming from the company's country are nationaly formatted. "
             "International numbers are always using international format."
    )
