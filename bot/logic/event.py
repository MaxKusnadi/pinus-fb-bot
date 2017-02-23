import logging

from bot.modelMappers.event import EventMapper


class EventLogic(object):

    def __init__(self):
        self.map = EventMapper()

    def get_all_events(self):
        events = self.map.get_all_events()
        for event in events:
            event.isActive = str(event.isActive)
        events = sorted(events, key=lambda x: x.id)
        return events

    def activate_event(self, event_id):
        try:
            self.map.set_event_active(event_id)
        except ValueError as err:
            logging.error(err)
            logging.error(err.args)

    def deactivate_event(self, event_id):
        try:
            self.map.set_event_inactive(event_id)
        except ValueError as err:
            logging.error(err)
            logging.error(err.args)
