import logging

from bot.database import Database
from bot.modelMappers import *
from bot.models.songRequest import SongRequest


class SongRequestMapper(object):

    # Create Request
    def create_request(self, song, message, url, title, artist):
        request = SongRequest(song, message, url, title, artist)
        Database.add_to_db(request)
        return request

    # Get Request
    def get_all_requests(self):
        u = SongRequest.query.all()
        return u
