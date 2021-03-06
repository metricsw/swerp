# -*- coding: utf-8 -*-
# Part of Swerp. See LICENSE file for full copyright and licensing details.

from swerp import api, fields, models


class StockWarnInsufficientQtyUnbuild(models.TransientModel):
    _name = 'stock.warn.insufficient.qty.unbuild'
    _inherit = 'stock.warn.insufficient.qty'
    _description = 'Warn Insufficient Unbuild Quantity'

    unbuild_id = fields.Many2one('mrp.unbuild', 'Unbuild')

    def action_done(self):
        self.ensure_one()
        return self.unbuild_id.action_unbuild()