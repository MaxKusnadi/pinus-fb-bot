from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app import db


class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    fb_id = Column(String)
    first_name = Column(String)
    last_name = Column(String)

    order = relationship("Order", backref="user")
    

    def __init__(self, fb_id, first_name="", last_name=""):
        self.fb_id = fb_id
        self.first_name = first_name
        self.last_name = last_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name  = last_name

    def __repr__(self):
        return '<id {} - {} {}>'.format(self.id, self.first_name, self.last_name)

class Order(db.Model):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True)
    time = Column(DateTime)
    status = Column(String)

    user_id = Column(Integer, ForeignKey('user.id'))
    order_item = relationship("OrderItem", backref="order")

    def __init__(self, user, time=None, status="NOT CONFIRMED"):
        self.time = time
        self.status = status
        self.user = user

    def set_time(self):
        import datetime

        self.time = datetime.datetime.utcnow()

    def set_status(self, status):
        self.status = status

    def __repr__(self):
        return '<id {} - Order by: {} Time: {} Status: {}>'.format(self.id,
                                                                   self.user_id,
                                                                   self.time,
                                                                   self.status)

class OrderItem(db.Model):
    __tablename__ = "order_item"

    id = Column(Integer, primary_key=True)
    description = Column(String)
    quantity = Column(Integer)

    order_id = Column(Integer, ForeignKey("order.id"))

    def __init__(self, description, quantity):
        self.description = description
        self.quantity = quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def __repr__(self):
        return '<id {} - Desc: {} Quantity: {}'.format(self.id,
                                                       self.description,
                                                       self.quantity)