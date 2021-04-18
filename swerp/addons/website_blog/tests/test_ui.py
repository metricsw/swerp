# Part of Swerp. See LICENSE file for full copyright and licensing details.

import swerp.tests


@swerp.tests.tagged('post_install', '-at_install')
class TestUi(swerp.tests.HttpCase):
    def test_admin(self):
        self.phantom_js("/", "swerp.__DEBUG__.services['web_tour.tour'].run('blog')", "swerp.__DEBUG__.services['web_tour.tour'].tours.blog.ready", login='admin')
