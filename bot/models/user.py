from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from  bot import db

import bot.models.order
import bot.constants.value

class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    fb_id = Column(String)
    first_name = Column(String)
    last_name = Column(String)

    order = relationship("Order", backref="user")
    

    def __init__(self, fb_id, first_name=EMPTY_STRING, last_name=EMPTY_STRING):
        self.fb_id = fb_id
        self.first_name = first_name
        self.last_name = last_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name  = last_name

    def __repr__(self):
        return '<id {} - {} {}>'.format(self.fb_id, self.first_name, self.last_name)