import unittest

from bot.models.songRequest import SongRequest


class TestSongRequest(unittest.TestCase):

    def test_set_get(self):
        song = SongRequest("abc song", "i miss u",
                           "spotify", "lost stars", "adam")

        assert(song.song == "abc song")
        assert(song.message == "i miss u")
        assert(song.url == "spotify")
        assert(song.title == "lost stars")
        assert(song.artist == "adam")
        assert(song.__repr__(
        ) == '<id {} - Song: {} Message: {}>'.format(song.id, "abc song", "i miss u"))
