import unittest

from bot.database import Database
from bot.modelMappers.user import UserMapper


class TestUserMapperCreate(unittest.TestCase):

    def setUp(self):
        Database.clear_db()
        self.mapper = UserMapper()

    def test_create_user(self):
        u = self.mapper.create_user("abc123", "Max", "Kusnadi")
        assert (u.fb_id == "abc123")
        assert (u.first_name == "Max")
        assert (u.last_name == "Kusnadi")

    def test_invalid_fb_id(self):
        self.assertRaises(ValueError, self.mapper.create_user, "@#`")

    def test_invalid_name(self):
        self.assertRaises(ValueError, self.mapper.create_user, "1234", "@#`")


class TestUserMapperRead(unittest.TestCase):

    def setUp(self):
        Database.clear_db()
        self.mapper = UserMapper()
        self.u = self.mapper.create_user("123456", "Max", "Kusnadi")


    def test_read_fb_id_valid(self):
        u = self.mapper.get_user_by_fb_id("123456")
        assert (u.first_name == "Max")

    def test_read_fb_id_invalid(self):
        self.assertRaises(ValueError, self.mapper.get_user_by_fb_id, "@34")

    def test_read_fb_id_not_found(self):
        self.assertRaises(ValueError, self.mapper.get_user_by_fb_id, "abc")

    
    def test_read_name_valid(self):
        u = self.mapper.get_user_by_name("Max")
        assert (u.fb_id == "123456")

    def test_read_full_name_valid(self):
        u = self.mapper.get_user_by_name("Max", "Kusnadi")
        assert (u.fb_id == "123456")

    def test_read_name_invalid(self):
        self.assertRaises(ValueError, self.mapper.get_user_by_name, "@34")

    def test_read_name_not_found(self):
        self.assertRaises(ValueError, self.mapper.get_user_by_name, "Marc")


    def test_read_all_user(self):
        u_list = self.mapper.get_all_users()
        assert (self.u in u_list)


class TestUserMapperUpdate(unittest.TestCase):

    def setUp(self):
        Database.clear_db()
        self.mapper = UserMapper()
        self.u = self.mapper.create_user("123", "Max", "Kusnadi")

    def test_set_first_name(self):
        u = self.mapper.set_first_name("123", "Cindy")
        assert(u.first_name == "Cindy")

    def test_set_first_name_invalid_fb_id(self):
        self.assertRaises(ValueError, self.mapper.set_first_name, "#$%", "Cindy")

    def test_set_last_name(self):
        u = self.mapper.set_last_name("123", "Cipu")
        assert(u.last_name == "Cipu")

    def test_set_last_name_invalid_fb_id(self):
        self.assertRaises(ValueError, self.mapper.set_last_name, "#$%", "Cindy")