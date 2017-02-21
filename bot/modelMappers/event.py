import logging

from bot.database import Database
from bot.constants.error import *
from bot.models.event import Event
from bot.modelMappers import *


class EventMapper(object):

    # CREATE
    def create_event(self, title, description=None, link=None):
        try:
            if is_input_not_empty(title):
                e = Event(title, description=description, link=link)
        except ValueError as err:
            logging.error(err)
            logging.error(err.args)
            raise ValueError(UNABLE_TO_CREATE.format("Event"), title)
        else:
            Database.add_to_db(e)
            return e

    # READ
    def get_event_by_id(self, event_id):
        e = Event.query.filter(Event.id == event_id).first()
        if e:
            return e
        else:
            raise ValueError(NOT_FOUND.format("Event"), event_id)

    def get_all_events(self):
        events = Event.query.all()
        return events

    def get_all_active_events(self):
        events = Event.query.filter(Event.isActive).all()
        return events

    # UPDATE
    def update_event(self, event_id, title=None, description=None):
        try:
            event = self.get_event_by_id(event_id)
        except ValueError as err:
            logging.error(err)
            logging.error(err.args)
            raise ValueError(NOT_FOUND.format("Event"), event_id)
        else:
            if title:
                event.update_title(title)
            if description:
                event.update_description(description)
            Database.commit_db()
            return event

    def set_event_inactive(self, event_id):
        try:
            event = self.get_event_by_id(event_id)
        except ValueError as err:
            logging.error(err)
            logging.error(err.args)
            raise ValueError(NOT_FOUND.format("Event"), event_id)
        else:
            event.set_inactive()
            Database.commit_db()
            return event

    def set_event_active(self, event_id):
        try:
            event = self.get_event_by_id(event_id)
        except ValueError as err:
            logging.error(err)
            logging.error(err.args)
            raise ValueError(NOT_FOUND.format("Event"), event_id)
        else:
            event.set_active()
            Database.commit_db()
            return event
