import logging
import json
import requests

from bot.modelMappers.songRequest import SongRequestMapper


class SongRequestLogic(object):

    def __init__(self):
        self.mapper = SongRequestMapper()

    def get_all_requests(self):
        songs = self.mapper.get_all_requests()
        return songs

    def process_message(self, message):
        text_list = message.split("//")
        try:
            song = text_list[0]
            message = "".join(text_list[1:])
        except:
            logging.error("Song input invalid")
            logging.error(message)
            return False

        if not song or not message:
            logging.error("Empty inputs")
            return False

        d = self._search_song(song)
        title = d['title']
        artist = d['artist']
        url = d['url']
        songs = self.mapper.create_request(song, message, url, title, artist)
        return songs

    def _search_song(self, song):
        link = 'https://api.spotify.com/v1/search?q={songs}&type=track'
        # Getting valid format for songs
        song_list = song.split(" ")
        song_final = "+".join(song_list)
        url = link.format(songs=song_final)
        r = requests.get(url)
        try:
            result = r.json()['tracks']
        except:
            logging.error("Cant find songs")
            d = {
                "url": "#",
                "artist": "Can't recommend anything",
                "title": ""
            }
            return d
        song_guess = result['items'][0]
        title = song_guess['name']
        artist = song_guess['artists'][0]['name']
        url = song_guess['external_urls']['spotify']
        d = {
            "url": url,
            "artist": artist,
            "title": title
        }
        return d
