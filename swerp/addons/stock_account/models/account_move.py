# -*- coding: utf-8 -*-

from swerp import fields, models, _

from swerp.tools.float_utils import float_is_zero

from swerp.exceptions import UserError

class AccountMove(models.Model):
    _inherit = 'account.move'

    stock_move_id = fields.Many2one('stock.move', string='Stock Move')
