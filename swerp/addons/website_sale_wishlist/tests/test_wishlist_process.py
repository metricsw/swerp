# -*- coding: utf-8 -*-
# Part of Swerp. See LICENSE file for full copyright and licensing details.
import swerp.tests


@swerp.tests.common.at_install(False)
@swerp.tests.common.post_install(True)
class TestUi(swerp.tests.HttpCase):
    def test_01_wishlist_tour(self):
        self.phantom_js("/", "swerp.__DEBUG__.services['web_tour.tour'].run('shop_wishlist')", "swerp.__DEBUG__.services['web_tour.tour'].tours.shop_wishlist.ready")
