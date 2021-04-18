import swerp.tests


@swerp.tests.tagged('post_install', '-at_install')
class TestUi(swerp.tests.HttpCase):
    def test_admin(self):
        self.phantom_js("/", "swerp.__DEBUG__.services['web_tour.tour'].run('event')", "swerp.__DEBUG__.services['web_tour.tour'].tours.event.ready", login='admin')
