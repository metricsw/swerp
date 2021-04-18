# -*- coding: utf-8 -*-
# Part of Swerp. See LICENSE file for full copyright and licensing details.

from swerp import models


class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = ['utm.mixin', 'sale.order']
