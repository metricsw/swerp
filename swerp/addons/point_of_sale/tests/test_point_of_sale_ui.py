# Part of Swerp. See LICENSE file for full copyright and licensing details.

import swerp.tests


@swerp.tests.tagged('post_install', '-at_install')
class TestUi(swerp.tests.HttpCase):

    def test_01_point_of_sale_tour(self):
        self.phantom_js("/web", "swerp.__DEBUG__.services['web_tour.tour'].run('point_of_sale_tour')", "swerp.__DEBUG__.services['web_tour.tour'].tours.point_of_sale_tour.ready", login="admin")
