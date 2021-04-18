# -*- coding: utf-8 -*

from swerp.addons.bus.controllers.main import BusController
from swerp.http import request


class CalendarBusController(BusController):
    # --------------------------
    # Extends BUS Controller Poll
    # --------------------------
    def _poll(self, dbname, channels, last, options):
        if request.session.uid:
            channels = list(channels)
            channels.append((request.db, 'calendar.alarm', request.env.user.partner_id.id))
        return super(CalendarBusController, self)._poll(dbname, channels, last, options)
