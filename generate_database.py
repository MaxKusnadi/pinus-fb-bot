from bot.modelMappers.event import EventMapper
from bot.modelMappers.songRequest import SongRequestMapper

e = EventMapper()
s = SongRequestMapper()

e.create_event("Nuansa")
e.create_event("Galigo")
e.create_event("MKP")

s.create_request("HEHE", "AJBVHXU",
                 "https://open.spotify.com/track/7rdGrVIoqwPWOULauvglio", "Lost Stars", "Adam Levine")
