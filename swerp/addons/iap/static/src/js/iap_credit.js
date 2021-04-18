swerp.define('iap.redirect_swerp_credit_widget', function(require) {
"use strict";

var AbstractAction = require('web.AbstractAction');
var core = require('web.core');


var IapSwerpCreditRedirect = AbstractAction.extend({
    template: 'iap.redirect_to_swerp_credit',
    events : {
        "click .redirect_confirm" : "swerp_redirect",
    },
    init: function (parent, action) {
        this._super(parent, action);
        this.url = action.params.url;
    },

    swerp_redirect: function () {
        window.open(this.url, '_blank');
        this.do_action({type: 'ir.actions.act_window_close'});
        // framework.redirect(this.url);
    },

});
core.action_registry.add('iap_swerp_credit_redirect', IapSwerpCreditRedirect);
});
