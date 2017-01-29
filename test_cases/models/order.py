import unittest

from bot import db
from bot.models.user import User
from bot.models.order import Order
from bot.models import clear_db

class TestOrder(unittest.TestCase):
    def setUp(self):
        clear_db()
        
    def test_create(self):
        user = User("abc")
        db.session.add(user)
        db.session.commit()

        order = Order(user)
        db.session.add(order)
        db.session.commit()

        orders = Order.query.all()
        self.assertTrue(order in orders)
        clear_db()


    def test_set_get(self):
        user = User("abc")
        db.session.add(user)
        db.session.commit()

        order = Order(user)
        db.session.add(order)
        db.session.commit()

        o = Order.query.filter(Order.user_id==user.id).first()
        assert(o.time == None)
        assert(o.status == "NOT CONFIRMED")

        o.set_time()
        o.set_status("CONFIRMED")
        db.session.commit()

        updated_o = Order.query.filter(Order.user_id==user.id).first()
        assert(updated_o.time != None)
        assert(updated_o.status == "CONFIRMED")
        assert(updated_o.__repr__() == '<id {} - Order by: {} Time: {} Status: {}>'.format(updated_o.id,
                                                                   user.id,
                                                                   updated_o.time,
                                                                   "CONFIRMED"))
        clear_db()

    def test_relationship(self):
        user = User("abc")
        db.session.add(user)
        db.session.commit()

        order = Order(user)
        db.session.add(order)
        db.session.commit()

        assert(order.user_id == user.id)
        assert(order in user.order)


