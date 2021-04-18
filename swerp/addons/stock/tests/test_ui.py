# -*- coding: utf-8 -*-
# Part of Swerp. See LICENSE file for full copyright and licensing details.

import swerp.tests

@swerp.tests.tagged('post_install', '-at_install')
class TestUi(swerp.tests.HttpCase):

    def test_01_admin_stock_route(self):
        self.phantom_js("/web", "swerp.__DEBUG__.services['web_tour.tour'].run('stock')", "swerp.__DEBUG__.services['web_tour.tour'].tours.stock.ready", login='admin')
