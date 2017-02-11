from sqlalchemy import Column, String, Integer, ForeignKey

from bot import db


class OrderItem(db.Model):
    __tablename__ = "order_item"

    id = Column(Integer, primary_key=True)
    description = Column(String)
    quantity = Column(Integer)

    order_id = Column(Integer, ForeignKey("order.id"))

    def __init__(self, order, description, quantity):
        self.description = description
        self.quantity = quantity
        self.order = order

    def set_quantity(self, quantity):
        self.quantity = quantity

    def __repr__(self):
        return '<id {} - Desc: {} Quantity: {}>'.format(self.id,
                                                       self.description,
                                                       self.quantity)