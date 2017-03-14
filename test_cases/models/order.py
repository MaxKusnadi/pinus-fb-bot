import unittest

from bot.constants.value import *
from bot.models.order import Order
from bot.models.user import User


class TestOrder(unittest.TestCase):

    def test_set_get(self):
        user = User("abc")
        order = Order(user, "Flower", 2)

        assert(order.time == None)
        assert(order.status == CONFIRMED)
        assert(order.description == "Flower")
        assert(order.quantity == 2)

        order.set_time_auto()
        order.set_status(NOT_CONFIRMED)

        assert(order.time != None)
        assert(order.status == NOT_CONFIRMED)
        assert(order.__repr__() == '<id {} - Order by: {} Time: {} Status: {} Description: {} Quantity: {} >'.format(order.id,
                                                                                                                     user.id,
                                                                                                                     order.time,
                                                                                                                     NOT_CONFIRMED,
                                                                                                                     "Flower",
                                                                                                                     2))

    def test_relationship(self):
        user = User("abc")
        order = Order(user, "Flower", 2)

        assert(order.user_id == user.id)
        assert(order in user.order)
