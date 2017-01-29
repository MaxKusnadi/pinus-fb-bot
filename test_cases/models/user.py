import unittest

from bot import db
from bot.models.user import User
from bot.models import clear_db

class TestUser(unittest.TestCase):
    def setUp(self):
        clear_db()
        
    def test_create(self):
        user = User("abcdef")
        db.session.add(user)
        db.session.commit()
        users = User.query.all()
        self.assertTrue(user in users)

    def test_set_get(self):
        user = User("abc")
        db.session.add(user)
        db.session.commit()

        u = User.query.filter(User.fb_id=="abc").first()
        assert(u.first_name == "")
        assert(u.last_name == "")

        u.set_first_name("Max")
        u.set_last_name("Kusnadi")
        db.session.commit()

        updated_u = User.query.filter(User.fb_id=="abc").first()
        assert(u.first_name == "Max")
        assert(u.last_name == "Kusnadi")
        assert(u.__repr__() == '<id abc - Max Kusnadi>')

