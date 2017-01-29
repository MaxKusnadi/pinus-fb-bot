import unittest

from bot import db
from bot.models.user import User
from bot.models.order import Order
from bot.models.orderItem import OrderItem
from bot.models import clear_db

class TestOrderItem(unittest.TestCase):
    def setUp(self):
        clear_db()
        
    def test_create(self):
        user = User("abc")
        db.session.add(user)
        db.session.commit()

        order = Order(user)
        db.session.add(order)
        db.session.commit()

        order_item = OrderItem(order, "FLOWER", 2)
        db.session.add(order_item)
        db.session.commit()

        order_items = OrderItem.query.all()
        self.assertTrue(order_item in order_items)
        clear_db()


    def test_set_get(self):
        user = User("abc")
        db.session.add(user)
        db.session.commit()

        order = Order(user)
        db.session.add(order)
        db.session.commit()

        order_item = OrderItem(order, "FLOWER", 2)
        db.session.add(order_item)
        db.session.commit()

        o = OrderItem.query.filter(OrderItem.order_id==order.id).first()
        assert(o.description == "FLOWER")
        assert(o.quantity == 2)

        o.set_quantity(3)
        db.session.commit()

        updated_o = OrderItem.query.filter(OrderItem.order_id==order.id).first()
        assert(updated_o.quantity == 3)
        assert(updated_o.__repr__() == '<id {} - Desc: {} Quantity: {}>'.format(updated_o.id,
                                                                   "FLOWER",
                                                                   3))
        clear_db()

    def test_relationship(self):
        user = User("abc")
        db.session.add(user)
        db.session.commit()

        order = Order(user)
        db.session.add(order)
        db.session.commit()

        order_item = OrderItem(order, "FLOWER", 2)
        db.session.add(order_item)
        db.session.commit()

        assert(order_item.order_id == order.id)
        assert(order_item in order.order_item)


