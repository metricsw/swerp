# -*- coding: utf-8 -*-
# Part of Swerp. See LICENSE file for full copyright and licensing details.

import swerp.tests


@swerp.tests.tagged('post_install', '-at_install')
class TestWebsiteCrm(swerp.tests.HttpCase):

    def test_tour(self):
        self.phantom_js("/", "swerp.__DEBUG__.services['web_tour.tour'].run('website_crm_tour')", "swerp.__DEBUG__.services['web_tour.tour'].tours.website_crm_tour.ready")

        # check result
        record = self.env['crm.lead'].search([('description', '=', '### TOUR DATA ###')])
        self.assertEqual(len(record), 1)
        self.assertEqual(record.contact_name, 'John Smith')
        self.assertEqual(record.email_from, 'john@smith.com')
        self.assertEqual(record.partner_name, 'Swerp S.A.')
