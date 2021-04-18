# -*- coding: utf-8 -*-

import swerp

def migrate(cr, version):
    registry = swerp.registry(cr.dbname)
    from swerp.addons.account.models.chart_template import migrate_tags_on_taxes
    migrate_tags_on_taxes(cr, registry)
