from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from bot import db

import bot.models.order


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