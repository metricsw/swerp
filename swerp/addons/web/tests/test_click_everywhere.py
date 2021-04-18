# Part of swerp. See LICENSE file for full copyright and licensing details.

import swerp.tests


@swerp.tests.tagged('click_all', 'post_install', '-at_install', '-standard')
class TestMenusAdmin(swerp.tests.HttpCase):

    def test_01_click_everywhere_as_admin(self):
        self.browser_js("/web", "swerp.__DEBUG__.services['web.clickEverywhere']();", "swerp.isReady === true", login="admin", timeout=45*60)


@swerp.tests.tagged('click_all', 'post_install', '-at_install', '-standard')
class TestMenusDemo(swerp.tests.HttpCase):

    def test_01_click_everywhere_as_demo(self):
        self.browser_js("/web", "swerp.__DEBUG__.services['web.clickEverywhere']();", "swerp.isReady === true", login="demo", timeout=1800)
