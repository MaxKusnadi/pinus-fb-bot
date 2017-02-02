from flask_restful import Resource

from bot import app, api

class Index(Resource):
	def get(self):
		return "Hello, World!"

api.add_resource(Index, '/')