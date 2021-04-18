# -*- coding: utf-8 -*-
# Part of Swerp. See LICENSE file for full copyright and licensing details.

from swerp import api, models, fields
from swerp.addons.http_routing.models.ir_http import slug
from swerp.tools.translate import html_translate


class ImLivechatChannel(models.Model):

    _name = 'im_livechat.channel'
    _inherit = ['im_livechat.channel', 'website.published.mixin']

    @api.multi
    def _compute_website_url(self):
        super(ImLivechatChannel, self)._compute_website_url()
        for channel in self:
            channel.website_url = "/livechat/channel/%s" % (slug(channel),)

    website_description = fields.Html("Website description", default=False, help="Description of the channel displayed on the website page", sanitize_attributes=False, translate=html_translate)
