# -*- coding: utf-8 -*-
# Part of Swerp. See LICENSE file for full copyright and licensing details.

from swerp.http import Controller, request, route


class DigestController(Controller):

    @route('/digest/<int:digest_id>/unsubscribe', type='http', website=True, auth='user')
    def digest_unsubscribe(self, digest_id, **post):
        digest = request.env['digest.digest'].sudo().browse(digest_id)
        digest.action_unsubcribe()
        return request.render('digest.portal_digest_unsubscribed', {
            'digest': digest,
        })
