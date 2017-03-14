import unittest

from bot.database import Database
from bot.modelMappers.order import OrderMapper
from bot.modelMappers.user import UserMapper


class TestOrderMapperCreate(unittest.TestCase):

    def setUp(self):
        Database.clear_db()
        uMapper = UserMapper()
        self.u = uMapper.create_user("123")
        self.mapper = OrderMapper()

    def test_create_order(self):
        order = self.mapper.create_order("123", "Flower", 2)

        assert (order.description == "Flower")
        assert (order.quantity == 2)
        assert (order.user_id == self.u.id)

    def test_create_order_invalid_fb_id(self):
        self.assertRaises(
            ValueError, self.mapper.create_order, "@#", "flower", 2)


class TestOrderMapperRead(unittest.TestCase):

    def setUp(self):
        Database.clear_db()
        self.uMapper = UserMapper()
        self.u = self.uMapper.create_user("123")
        self.mapper = OrderMapper()
        self.o = self.mapper.create_order("123", "Flower", 2)

    def test_get_order_by_order_id(self):
        order = self.mapper.get_order_by_order_id(self.o.id)
        assert (order.user_id == self.u.id)

    def test_get_order_by_invalid_order_id(self):
        self.assertRaises(ValueError, self.mapper.get_order_by_order_id, 123)

    def test_get_order_by_fb_id(self):
        orders = self.mapper.get_orders_by_fb_id("123")
        assert(self.o in orders)

    def test_get_order_by_invalid_fb_id(self):
        self.assertRaises(ValueError, self.mapper.get_orders_by_fb_id, "233")

    def test_get_order_by_fb_id_no_order(self):
        self.uMapper.create_user("456")
        self.assertRaises(ValueError, self.mapper.get_orders_by_fb_id, "456")


class TestOrderMapperUpdate(unittest.TestCase):

    def setUp(self):
        Database.clear_db()
        uMapper = UserMapper()
        u = uMapper.create_user("123")
        self.mapper = OrderMapper()
        self.o = self.mapper.create_order("123", "Flower", 2)

    def test_update_status_by_order_id(self):
        order = self.mapper.update_order_status_by_order_id(
            self.o.id, "NOT_CONFIRMED")
        assert(order.status == "NOT_CONFIRMED")

    def test_update_status_by_invalid_order_id(self):
        self.assertRaises(
            ValueError, self.mapper.update_order_status_by_order_id, 12345, "HELLO")
