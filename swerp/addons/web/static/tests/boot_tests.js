(function() {
"use strict";

swerp.__DEBUG__.didLogInfo.then(function() {

    var modulesInfo = swerp.__DEBUG__.js_modules;

    QUnit.module('swerp JS Modules');

    QUnit.test('all modules are properly loaded', function(assert) {
        assert.expect(2);

        assert.deepEqual(modulesInfo.missing, [],
            "no js module should be missing");
        assert.deepEqual(modulesInfo.failed, [],
            "no js module should have failed");
    });

});

})();