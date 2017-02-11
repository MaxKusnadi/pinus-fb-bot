import unittest

from bot.constants.value import *
from bot.models.order import Order
from bot.models.user import User

class TestOrder(unittest.TestCase):

    def test_set_get(self):
        user = User("abc")
        order = Order(user)

        assert(order.time == None)
        assert(order.status == NOT_CONFIRMED)

        order.set_time_auto()
        order.set_status(CONFIRMED)

        assert(order.time != None)
        assert(order.status == CONFIRMED)
        assert(order.__repr__() == '<id {} - Order by: {} Time: {} Status: {}>'.format(order.id,
                                                                   user.id,
                                                                   order.time,
                                                                   CONFIRMED))
        
        import datetime
        time = datetime.datetime.utcnow()
        order.set_time_manual(time)

        assert(order.time == time)

    def test_relationship(self):
        user = User("abc")
        order = Order(user)

        assert(order.user_id == user.id)
        assert(order in user.order)


