# Part of Swerp. See LICENSE file for full copyright and licensing details.

import swerp.tests

@swerp.tests.common.tagged('post_install', '-at_install')
class TestUi(swerp.tests.HttpCase):

    def test_01_admin_forum_tour(self):
        self.phantom_js("/", "swerp.__DEBUG__.services['web_tour.tour'].run('question')", "swerp.__DEBUG__.services['web_tour.tour'].tours.question.ready", login="admin")

    def test_02_demo_question(self):
        forum = self.env.ref('website_forum.forum_help')
        demo = self.env.ref('base.user_demo')
        demo.karma = forum.karma_post + 1
        self.phantom_js("/", "swerp.__DEBUG__.services['web_tour.tour'].run('forum_question')", "swerp.__DEBUG__.services['web_tour.tour'].tours.forum_question.ready", login="demo")
