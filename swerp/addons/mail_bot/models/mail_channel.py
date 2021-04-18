# -*- coding: utf-8 -*-
# Part of Swerp. See LICENSE file for full copyright and licensing details.

from swerp import api, models, _


class Channel(models.Model):
    _inherit = 'mail.channel'

    def _execute_command_help(self, **kwargs):
        super(Channel, self)._execute_command_help(**kwargs)
        self.env['mail.bot']._apply_logic(self, kwargs, command="help")  # kwargs are not usefull but...

    @api.model
    def init_swerpbot(self):
        if self.env.user.swerpbot_state == 'not_initialized':
            partner = self.env.user.partner_id
            swerpbot_id = self.env['ir.model.data'].xmlid_to_res_id("base.partner_root")
            channel = self.with_context(mail_create_nosubscribe=True).create({
                'channel_partner_ids': [(4, partner.id), (4, swerpbot_id)],
                'public': 'private',
                'channel_type': 'chat',
                'email_send': False,
                'name': 'SwerpBot'
            })
            message = _("Hello,<br/>Swerp's chat helps employees collaborate efficiently. I'm here to help you discover its features.<br/><b>Try to send me an emoji :)</b>")
            channel.sudo().message_post(body=message, author_id=swerpbot_id, message_type="comment", subtype="mail.mt_comment")
            self.env.user.swerpbot_state = 'onboarding_emoji'
            return channel
