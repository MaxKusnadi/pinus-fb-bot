import logging


from flask import render_template
from bot import app
from bot.logic.songRequest import SongRequestLogic


logic = SongRequestLogic()


@app.route('/san-song-request', methods=['GET'])
def song_request():
    songs = logic.get_all_requests()
    return render_template('songRequest/index.html', songs=songs)
