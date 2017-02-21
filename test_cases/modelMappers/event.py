import unittest

from bot.database import Database
from bot.modelMappers.event import EventMapper


class TestEventMapperCreate(unittest.TestCase):

    def setUp(self):
        Database.clear_db()
        self.map = EventMapper()

    def test_create_valid_event(self):
        e = self.map.create_event(
            "galigo", description="Hello", link="mama.com")

        assert(e.title == "galigo")
        assert(e.description == "Hello")
        assert(e.link == "mama.com")

    def test_create_invalid_event(self):
        self.assertRaises(ValueError, self.map.create_event, "")


class TestEventMapperRead(unittest.TestCase):

    def setUp(self):
        Database.clear_db()
        self.map = EventMapper()
        self.active_1 = self.map.create_event(
            "galigo")
        self.active_2 = self.map.create_event(
            "nuansa")
        self.inactive_1 = self.map.create_event(
            "popi")
        self.inactive_2 = self.map.create_event(
            "mkp")
        self.inactive_1 = self.map.set_event_inactive(self.inactive_1.id)
        self.inactive_2 = self.map.set_event_inactive(self.inactive_2.id)

    def test_get_event_by_id(self):
        event_id = self.active_1.id
        e = self.map.get_event_by_id(event_id)
        assert(e.title == "galigo")

    def test_get_event_by_invalid_id(self):
        self.assertRaises(ValueError, self.map.get_event_by_id, -1)

    def test_get_all_events(self):
        events = self.map.get_all_events()
        assert(self.active_1 in events)
        assert(self.active_2 in events)
        assert(self.inactive_1 in events)
        assert(self.inactive_2 in events)

    def test_get_all_active_events(self):
        events = self.map.get_all_active_events()
        assert(self.active_1 in events)
        assert(self.active_2 in events)
        assert(self.inactive_1 not in events)
        assert(self.inactive_2 not in events)


class TestEventMapperUpdate(unittest.TestCase):

    def setUp(self):
        Database.clear_db()
        self.map = EventMapper()
        self.e = self.map.create_event(
            "galigo")

    def test_update_event(self):
        e = self.map.update_event(
            self.e.id, title="Nuansa", description="Hello")
        e = self.map.get_event_by_id(e.id)
        assert(e.title == "Nuansa")
        assert(e.description == "Hello")

    def test_set_event_inactive(self):
        e = self.map.set_event_inactive(self.e.id)
        e = self.map.get_event_by_id(e.id)
        assert(e.isActive is False)

    def test_set_event_active(self):
        e = self.map.set_event_active(self.e.id)
        e = self.map.get_event_by_id(e.id)
        assert(e.isActive is True)

    def test_update_event_invalid(self):
        self.assertRaises(ValueError, self.map.update_event, -1)

    def test_set_event_inactive_invalid(self):
        self.assertRaises(ValueError, self.map.set_event_inactive, -1)

    def test_set_event_active_invalid(self):
        self.assertRaises(ValueError, self.map.set_event_active, -1)
