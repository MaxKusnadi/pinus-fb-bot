import logging


from flask import render_template
from bot import app
from bot.logic.logic import Logic


logic = Logic()


@app.route('/admin', methods=['GET'])
def index():
    return render_template('index.html')
