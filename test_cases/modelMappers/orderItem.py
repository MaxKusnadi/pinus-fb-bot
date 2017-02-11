import unittest

from bot.database import Database
from bot.modelMappers.orderItem import OrderItemMapper
from bot.modelMappers.order import OrderMapper
from bot.modelMappers.user import UserMapper


class TestOrderItemCreate(unittest.TestCase):
    def setUp(self):
        Database.clear_db()
        uMapper = UserMapper()
        oMapper = OrderMapper()
        uMapper.create_user("123")
        self.o = oMapper.create_order("123")
        self.mapper = OrderItemMapper()

    def test_create_order_item_valid(self):
        oI = self.mapper.create_order_item(self.o.id, "Flower", 10)
        assert(oI.order_id == self.o.id)
        assert(oI.description == "Flower")
        assert(oI.quantity == 10)

    def test_create_order_item_invalid_order_id(self):
        self.assertRaises(ValueError, self.mapper.create_order_item, 100, "Flower", 10)

    def test_create_order_item_invalid_quantity(self):
        self.assertRaises(ValueError, self.mapper.create_order_item, self.o.id, "Flower", -1)



class TestOrderItemRead(unittest.TestCase):
    def setUp(self):
        Database.clear_db()
        uMapper = UserMapper()
        oMapper = OrderMapper()
        uMapper.create_user("123")
        self.o = oMapper.create_order("123")
        self.mapper = OrderItemMapper()
        self.oI = self.mapper.create_order_item(self.o.id, "Flo", 10)

    def test_read_order_item_by_order_id(self):
        items = self.mapper.get_order_items_by_order_id(self.o.id)
        assert(self.oI in items)

    def test_read_order_item_by_invalid_order_id(self):
        self.assertRaises(ValueError, self.mapper.get_order_items_by_order_id, 123)

    def test_read_order_item_by_id(self):
        oI = self.mapper.get_order_item_by_id(self.oI.id)
        assert(oI.description == "Flo")

    def test_read_order_item_by_invalid_id(self):
        self.assertRaises(ValueError, self.mapper.get_order_item_by_id, 123)



class TestOrderItemUpdate(unittest.TestCase):
    def setUp(self):
        Database.clear_db()
        uMapper = UserMapper()
        oMapper = OrderMapper()
        uMapper.create_user("123")
        self.o = oMapper.create_order("123")
        self.mapper = OrderItemMapper()
        self.oI = self.mapper.create_order_item(self.o.id, "Flo", 10)

    def test_update_order_item(self):
        oI = self.mapper.update_order_item_quantity_by_order_item_id(self.oI.id, 19)
        assert(oI.quantity == 19)

    def test_update_order_item_invalid_order_id(self):
        self.assertRaises(ValueError, self.mapper.update_order_item_quantity_by_order_item_id, 1293, 55)
        oI = self.mapper.get_order_items_by_order_id(self.oI.id)
        assert(oI.quantity == 19)

    def test_update_order_item_invalid_order_id(self):
        self.assertRaises(ValueError, self.mapper.update_order_item_quantity_by_order_item_id, self.oI.id, -1)

