# coding: utf-8

from swerp import fields, models


class PaymentAcquirer(models.Model):
    _inherit = 'payment.acquirer'

    website_id = fields.Many2one('website', ondelete='restrict')
