# -*- coding: utf-8 -*-
# Part of Swerp. See LICENSE file for full copyright and licensing details.

from swerp import models, fields


class Users(models.Model):
    _inherit = 'res.users'
    swerpbot_state = fields.Selection(
        selection_add=[
            ('onboarding_canned', 'Onboarding canned'),
        ])
