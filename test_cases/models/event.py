import unittest

from bot.models.event import Event
from bot.database import Database


class TestEvent(unittest.TestCase):

    def setUp(self):
        Database.clear_db()

    def test_create(self):
        title = "Nuansa"
        desc = "Nuansa is good"
        link = " www.nuansa.com"

        e = Event(title, description=desc, link=link)

        assert(e.title == title)
        assert(e.description == desc)
        assert(e.link == link)
        assert(e.creationDate is not None)
        assert(e.isActive is True)
        assert(e.__repr__() == 'ID: {id}, Title: {title}, Description: {desc}, Link: {link}, isActive: {isActive}'.format(
            id=e.id, title=title, desc=desc, link=link, isActive=True))

    def test_update(self):

        title = "Nuansa"

        e = Event(title)

        new_title = "Gaya"
        desc = "Gaya is good"
        link = "www.gaya.com"

        e.update_title(new_title)
        e.update_description(desc)
        e.update_link(link)
        e.set_inactive()

        assert(e.title == new_title)
        assert(e.description == desc)
        assert(e.link == link)
        assert(e.isActive is False)

        e.set_active()

        assert(e.isActive is True)
