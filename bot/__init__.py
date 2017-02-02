from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
import os

import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)

import bot.views.index

import bot.models.user
import bot.models.order
import bot.models.orderItem