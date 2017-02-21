import unittest

from bot.modelMappers import *


class TestInputChecker(unittest.TestCase):

    def test_user_args_valid(self):
        check = is_user_args_valid("123", "Max", "Kusnadi")
        self.assertTrue(check)

    def test_user_name_invalid(self):
        self.assertRaises(ValueError, is_user_args_valid, "123", "Max#@", "")

    def test_user_fb_id_invalid(self):
        self.assertRaises(ValueError, is_user_args_valid,
                          "123@$", "", "KUSNAID")

    def test_quantity_valid(self):
        check = is_quantity_valid(123)
        self.assertTrue(check)

    def test_quantity_invalid(self):
        self.assertRaises(ValueError, is_quantity_valid, -1)

    def test_input_not_empty(self):
        check = is_input_not_empty("hi")
        self.assertTrue(check)

    def test_input_empty(self):
        self.assertRaises(ValueError, is_input_not_empty, "")
