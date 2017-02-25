import logging

from bot.modelMappers.event import EventMapper


class EventLogic(object):

    def __init__(self):
        self.map = EventMapper()

    def create_event(self, title, description=None, link=None):
        try:
            event = self.map.create_event(title, description, link)
        except ValueError as err:
            logging.error(err)
            logging.error(err.args)
            event = None

        return event

    def update_event(self, event_id, title=None, description=None, link=None):
        try:
            event = self.map.update_event(event_id, title, description, link)
        except ValueError as err:
            logging.error(err)
            logging.error(err.args)
            event = None

        return event

    def get_event_by_id(self, event_id):
        try:
            event = self.map.get_event_by_id(event_id)
        except ValueError as err:
            logging.error(err)
            logging.error(err.args)
            event = None
        return event

    def get_all_events(self):
        events = self.map.get_all_events()

        def convert_to_string(event):
            event.isActive = str(event.isActive)
        events = map(lambda x: convert_to_string(x), events)
        # for event in events:
        #     event.isActive = str(event.isActive)
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
