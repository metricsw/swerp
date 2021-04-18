# -*- coding: utf-8 -*-
# Part of Swerp. See LICENSE file for full copyright and licensing details.

import swerp.tests

@swerp.tests.tagged('post_install', '-at_install')
class TestUi(swerp.tests.HttpCase):

    def test_01_admin_rte(self):
        self.phantom_js("/web", "swerp.__DEBUG__.services['web_tour.tour'].run('rte')", "swerp.__DEBUG__.services['web_tour.tour'].tours.rte.ready", login='admin')

    def test_02_admin_rte_inline(self):
        self.phantom_js("/web", "swerp.__DEBUG__.services['web_tour.tour'].run('rte_inline')", "swerp.__DEBUG__.services['web_tour.tour'].tours.rte_inline.ready", login='admin')
