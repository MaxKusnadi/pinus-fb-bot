import unittest

from bot.database import Database
from bot.modelMappers.songRequest import SongRequestMapper


class TestSongRequestMapperCreate(unittest.TestCase):

    def setUp(self):
        Database.clear_db()
        self.mapper = SongRequestMapper()

    def test_create_song(self):
        s = self.mapper.create_request(
            "song", "message", "url", "title", "artist")

        assert(s.song == "song")
        assert(s.message == "message")
        assert(s.url == "url")
        assert(s.title == "title")
        assert(s.artist == "artist")


class TestSongRequestMapperRead(unittest.TestCase):

    def setUp(self):
        Database.clear_db()
        self.mapper = SongRequestMapper()
        self.song_1 = self.mapper.create_request(
            "song", "message", "url", "title", "artist")
        self.song_2 = self.mapper.create_request(
            "songa", "messagea", "urla", "titleaa", "artistaa")

    def test_get_all_songs(self):
        songs = self.mapper.get_all_requests()

        assert(self.song_1 in songs)
        assert(self.song_2 in songs)
