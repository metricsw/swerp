# -*- coding: utf-8 -*-

import swerp

def migrate(cr, version):
    registry = swerp.registry(cr.dbname)
    from swerp.addons.account.models.chart_template import migrate_set_tags_and_taxes_updatable
    migrate_set_tags_and_taxes_updatable(cr, registry, 'l10n_hr')
