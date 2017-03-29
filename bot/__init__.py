import logging
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import bot.views.index
import bot.views.facebook
import bot.views.event
import bot.views.shop
import bot.views.songRequest

import bot.models.user
import bot.models.order
import bot.models.event
import bot.models.songRequest
