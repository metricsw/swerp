# -*- coding: utf-8 -*-
# Part of Swerp. See LICENSE file for full copyright and licensing details.

from . import models
from . import controllers
from swerp.addons.payment.models.payment_acquirer import create_missing_journal_for_acquirers
from swerp.addons.payment import reset_payment_provider

def uninstall_hook(cr, registry):
    reset_payment_provider(cr, registry, 'paypal')
