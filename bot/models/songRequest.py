from sqlalchemy import Column, String, Integer

from bot import db
from bot.constants.value import *


class SongRequest(db.Model):
    __tablename__ = 'songRequest'

    id = Column(Integer, primary_key=True)
    song = Column(String)
    message = Column(String)
    url = Column(String)
    title = Column(String)
    artist = Column(String)

    def __init__(self, song, message, url, title, artist):
        self.song = song
        self.message = message
        self.url = url
        self.title = title
        self.artist = artist

    def __repr__(self):
        return '<id {} - Song: {} Message: {}>'.format(self.id, self.song, self.message)
