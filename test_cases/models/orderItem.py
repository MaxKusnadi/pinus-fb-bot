import unittest

from bot.constants.value import *
from bot.models.user import User
from bot.models.order import Order
from bot.models.orderItem import OrderItem


class TestOrderItem(unittest.TestCase):
        
    def test_set_get(self):
        user = User("abc")
        order = Order(user)
        order_item = OrderItem(order, "FLOWER", 2)

        assert(order_item.description == "FLOWER")
        assert(order_item.quantity == 2)

        order_item.set_quantity(3)

        assert(order_item.quantity == 3)
        assert(order_item.__repr__() == '<id {} - Desc: {} Quantity: {}>'.format(order_item.id,
                                                                   "FLOWER",
                                                                   3))

    def test_relationship(self):
        user = User("abc")
        order = Order(user)
        order_item = OrderItem(order, "FLOWER", 2)

        assert(order_item.order_id == order.id)
        assert(order_item in order.order_item)


