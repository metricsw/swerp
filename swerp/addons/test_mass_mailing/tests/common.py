# -*- coding: utf-8 -*-
# Part of Swerp. See LICENSE file for full copyright and licensing details.

from swerp.addons.test_mail.tests import common
from swerp.addons.test_mail.tests.common import mail_new_test_user
from swerp.tests import tagged


@tagged('mass_mail')
class MassMailingCase(common.MockEmails, common.BaseFunctionalTest):

    @classmethod
    def setUpClass(cls):
        super(MassMailingCase, cls).setUpClass()

        # be sure for some common data
        cls.user_employee.write({
            'login': 'emp',
        })

        cls.user_marketing = mail_new_test_user(
            cls.env, login='marketing',
            groups='base.group_user,mass_mailing.group_mass_mailing_user',
            name='Martial Marketing', signature='--\nMartial')
