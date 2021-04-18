# Part of Swerp. See LICENSE file for full copyright and licensing details.

import swerp.tests


@swerp.tests.tagged('post_install', '-at_install')
class TestUi(swerp.tests.HttpCase):

    def test_01_project_tour(self):
        self.phantom_js("/web", "swerp.__DEBUG__.services['web_tour.tour'].run('project_tour')", "swerp.__DEBUG__.services['web_tour.tour'].tours.project_tour.ready", login="admin")
