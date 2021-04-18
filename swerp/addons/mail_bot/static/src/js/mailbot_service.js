swerp.define('mail_bot.MailBotService', function (require) {
"use strict";

var AbstractService = require('web.AbstractService');
var core = require('web.core');
var session = require('web.session');

var _t = core._t;

var MailBotService =  AbstractService.extend({
    /**
     * @override
     */
    start: function () {
        this._hasRequest = (window.Notification && window.Notification.permission === "default") || false;
        if ('swerpbot_initialized' in session && ! session.swerpbot_initialized) {
            this._showSwerpbotTimeout();
        }
    },

    //--------------------------------------------------------------------------
    // Public
    //--------------------------------------------------------------------------

    /**
     * Get the previews related to the SwerpBot (conversation not included).
     * For instance, when there is no conversation with SwerpBot and SwerpBot has
     * a request, it should display a preview in the systray messaging menu.
     *
     * @param {string|undefined} [filter]
     * @returns {Object[]} list of objects that are compatible with the
     *   'mail.Preview' template.
     */
    getPreviews: function (filter) {
        var previews = [];
        if (this.hasRequest() && (filter === 'mailbox_inbox' || !filter)) {
            previews.push({
                title: _t("SwerpBot has a request"),
                imageSRC: "/mail/static/src/img/swerpbot.png",
                status: 'bot',
                body:  _t("Enable desktop notifications to chat"),
                id: 'request_notification',
                unreadCounter: 1,
            });
        }
        return previews;
    },
    /**
     * Tell whether SwerpBot has a request or not.
     *
     * @returns {boolean}
     */
    hasRequest: function () {
        return this._hasRequest;
    },
    /**
     * Called when user either accepts or refuses push notifications.
     */
    removeRequest: function () {
        this._hasRequest = false;
    },

    //--------------------------------------------------------------------------
    // Private
    //--------------------------------------------------------------------------

    /**
     * @private
     */
    _showSwerpbotTimeout: function () {
        var self = this;
        setTimeout(function () {
            session.swerpbot_initialized = true;
            self._rpc({
                model: 'mail.channel',
                method: 'init_swerpbot',
            });
        }, 2*60*1000);
    },
});

core.serviceRegistry.add('mailbot_service', MailBotService);
return MailBotService;

});
