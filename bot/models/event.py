from datetime import datetime, tzinfo
from sqlalchemy import Column, String, Integer, Text, DateTime, Boolean
from bot import db
from bot.constants.value import *


class Event(db.Model):
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    link = Column(String)
    creationDate = Column(DateTime)
    isActive = Column(Boolean)

    def __init__(self, title, description=None, link=None, isActive=True):
        self.title = title
        self.description = description
        self.link = link
        self.creationDate = datetime.now()
        self.isActive = isActive

    def update_title(self, title):
        self.title = title

    def update_description(self, description):
        self.description = description

    def update_link(self, link):
        self.link = link

    def set_inactive(self):
        self.isActive = False

    def set_active(self):
        self.isActive = True

    def __repr__(self):
        return 'ID: {id}, Title: {title}, Description: {desc}, Link: {link}, isActive: {isActive}'.format(
            id=self.id, title=self.title, desc=self.description, link=self.link, isActive=self.isActive)
