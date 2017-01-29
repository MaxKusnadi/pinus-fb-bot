from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app import db


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