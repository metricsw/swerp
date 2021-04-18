# -*- coding: utf-8 -*-
# Part of Swerp. See LICENSE file for full copyright and licensing details.

from swerp import fields, models


class MrpBom(models.Model):
    _name = 'mrp.bom'
    _description = 'Bill of Material'
    _inherit = 'mrp.bom'

    sub_products = fields.One2many('mrp.subproduct', 'bom_id', 'Byproducts', copy=True)
