import unittest

from bot.models.user import User

class TestUser(unittest.TestCase):


    def test_set_get(self):
        user = User("abc")

        assert(user.fb_id == "abc")
        assert(user.first_name == "")
        assert(user.last_name == "")

        user.set_first_name("Max")
        user.set_last_name("Kusnadi")

        assert(user.first_name == "Max")
        assert(user.last_name == "Kusnadi")
        assert(user.__repr__() == '<id abc - Max Kusnadi>')


