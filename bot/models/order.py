from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from bot import db
from bot.constants.value import *


class Order(db.Model):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True)
    time = Column(DateTime)
    description = Column(String)
    quantity = Column(Integer)
    status = Column(String)

    user_id = Column(Integer, ForeignKey('user.id'))

    def __init__(self, user, description, quantity, status=CONFIRMED):
        self.time = None
        self.user = user
        self.description = description
        self.quantity = quantity
        self.status = status

    def set_time_auto(self):
        import datetime
        self.time = datetime.datetime.utcnow()

    def set_status(self, status):
        self.status = status

    def __repr__(self):
        return '<id {} - Order by: {} Time: {} Status: {} Description: {} Quantity: {} >'.format(self.id,
                                                                                                 self.user_id,
                                                                                                 self.time,
                                                                                                 self.status,
                                                                                                 self.description,
                                                                                                 self.quantity)
