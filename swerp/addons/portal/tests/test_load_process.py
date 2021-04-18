# -*- coding: utf-8 -*-
# Part of Swerp. See LICENSE file for full copyright and licensing details.
import swerp.tests


@swerp.tests.tagged('post_install', '-at_install')
class TestUi(swerp.tests.HttpCase):
    def test_01_portal_load_tour(self):
        self.phantom_js(
            "/",
            "swerp.__DEBUG__.services['web_tour.tour'].run('portal_load_homepage')",
            "swerp.__DEBUG__.services['web_tour.tour'].tours.portal_load_homepage.ready",
            login="portal"
        )
