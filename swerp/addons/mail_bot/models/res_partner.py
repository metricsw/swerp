# -*- coding: utf-8 -*-
# Part of Swerp. See LICENSE file for full copyright and licensing details.
from swerp import api, models

class Partner(models.Model):
    _inherit = 'res.partner'

    def _compute_im_status(self):
        #we asume that mail_bot _compute_im_status will be executed after bus _compute_im_status
        super(Partner, self)._compute_im_status()
        swerpbot_id = self.env['ir.model.data'].xmlid_to_res_id("base.partner_root")
        for partner in self:
            if partner.id == swerpbot_id:
                partner.im_status = 'bot'

    @api.model
    def get_mention_suggestions(self, search, limit=8):
        #add swerpbot in mention suggestion when pinging in mail_thread
        [users, partners] = super(Partner, self).get_mention_suggestions(search, limit=limit)
        if len(partners) + len(users) < limit and "swerpbot".startswith(search.lower()):
            swerpbot = self.env.ref("base.partner_root")
            if not any([elem['id'] == swerpbot.id for elem in partners]):
                if swerpbot:
                    partners.append({'id': swerpbot.id, 'name': swerpbot.name, 'email': swerpbot.email})
        return [users, partners]

