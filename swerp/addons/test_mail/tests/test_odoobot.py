# -*- coding: utf-8 -*-
# Part of Swerp. See LICENSE file for full copyright and licensing details.

from unittest.mock import patch

from swerp.addons.test_mail.tests.common import BaseFunctionalTest, MockEmails, TestRecipients
from swerp.tools import mute_logger
from swerp.tests import tagged


@tagged("swerpbot")
class TestSwerpbot(BaseFunctionalTest, MockEmails, TestRecipients):

    def setUp(self):
        super(TestSwerpbot, self).setUp()
        self.swerpbot = self.env.ref("base.partner_root")
        self.message_post_default_kwargs = {
            'body': '',
            'attachment_ids': [],
            'message_type': 'comment',
            'partner_ids': [],
            'subtype': 'mail.mt_comment'
        }
        self.swerpbot_ping_body = '<a href="http://swerp.it/web#model=res.partner&amp;id=%s" class="o_mail_redirect" data-oe-id="%s" data-oe-model="res.partner" target="_blank">@SwerpBot</a>' % (self.swerpbot.id, self.swerpbot.id)
        self.test_record_employe = self.test_record.sudo(self.user_employee)

    @mute_logger('swerp.addons.mail.models.mail_mail')
    def test_fetch_listener(self):
        channel = self.env['mail.channel'].sudo(self.user_employee).init_swerpbot()
        partners = self.env['mail.channel'].channel_fetch_listeners(channel.uuid)
        swerpbot = self.env.ref("base.partner_root")
        swerpbot_in_fetch_listeners = [partner for partner in partners if partner['id'] == swerpbot.id]
        self.assertEqual(len(swerpbot_in_fetch_listeners), 1, 'swerpbot should appear only once in channel_fetch_listeners')

    @mute_logger('swerp.addons.mail.models.mail_mail')
    def test_swerpbot_ping(self):
        kwargs = self.message_post_default_kwargs.copy()
        kwargs.update({'body': self.swerpbot_ping_body, 'partner_ids': [self.swerpbot.id, self.user_admin.partner_id.id]})

        with patch('random.choice', lambda x: x[0]):
            self.assertNextMessage(
                self.test_record_employe.with_context({'mail_post_autofollow': True}).message_post(**kwargs),
                sender=self.swerpbot,
                answer=["Yep, SwerpBot is in the place!"]
            )
        # Swerpbot should not be a follower but user_employee and user_admin should
        follower = self.test_record.message_follower_ids.mapped('partner_id')
        self.assertNotIn(self.swerpbot, follower)
        self.assertIn(self.user_employee.partner_id, follower)
        self.assertIn(self.user_admin.partner_id, follower)

    @mute_logger('swerp.addons.mail.models.mail_mail')
    def test_onboarding_flow(self):
        kwargs = self.message_post_default_kwargs.copy()
        channel = self.env['mail.channel'].sudo(self.user_employee).init_swerpbot()

        kwargs['body'] = 'tagada 😊'
        self.assertNextMessage(
            channel.message_post(**kwargs),
            sender=self.swerpbot,
            answer=("attachment",)
        )
        kwargs['body'] = ''
        kwargs['attachment_ids'] = [1]
        last_message = self.assertNextMessage(
            channel.message_post(**kwargs),
            sender=self.swerpbot,
            answer=("help",)
        )
        kwargs['attachment_ids'] = []

        channel.execute_command(command="help")
        self.assertNextMessage(
            last_message,  # no message will be post with command help, use last swerpbot message instead
            sender=self.swerpbot,
            answer=("@SwerpBot",)
        )
        # we dont test the end of the flow since it will depends of the installed apps (livechat)
        self.user_employee.swerpbot_state = "idle"
        kwargs['partner_ids'] = []
        kwargs['body'] = "I love you"
        self.assertNextMessage(
            channel.message_post(**kwargs),
            sender=self.swerpbot,
            answer=("too human for me",)
        )
        kwargs['body'] = "Go fuck yourself"
        self.assertNextMessage(
            channel.message_post(**kwargs),
            sender=self.swerpbot,
            answer=("I have feelings",)
        )

    @mute_logger('swerp.addons.mail.models.mail_mail')
    def test_swerpbot_no_default_answer(self):
        kwargs = self.message_post_default_kwargs.copy()
        kwargs.update({'body': "I'm not talking to @swerpbot right now", 'partner_ids': []})
        self.assertNextMessage(
            self.test_record_employe.message_post(**kwargs),
            answer=False
        )

    def assertNextMessage(self, message, answer=None, sender=None):
        last_message = self.env['mail.message'].search([('id', '=', message.id + 1)])
        if last_message:
            body = last_message.body.replace('<p>', '').replace('</p>', '')
        else:
            self.assertFalse(answer, "No last message found when an answer was expect")
        if answer is not None:
            if answer and not last_message:
                self.assertTrue(False, "No last message found")
            if isinstance(answer, list):
                self.assertIn(body, answer)
            elif isinstance(answer, tuple):
                for elem in answer:
                    self.assertIn(elem, body)
            elif not answer:
                self.assertFalse(last_message, "No answer should have been post")
                return
            else:
                self.assertEqual(body, answer)
        if sender:
            self.assertEqual(sender, last_message.author_id)
        return last_message
