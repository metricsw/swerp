# -*- coding: utf-8 -*-
# Part of Swerp. See LICENSE file for full copyright and licensing details.

from swerp import models


class PaymentWizard(models.TransientModel):
    _inherit = 'payment.acquirer.onboarding.wizard'
    _name = 'website.sale.payment.acquirer.onboarding.wizard'

    def _set_payment_acquirer_onboarding_step_done(self):
        """ Override. """
        self.env.user.company_id.set_onboarding_step_done('website_sale_onboarding_payment_acquirer_state')
