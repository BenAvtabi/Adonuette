from flask import jsonify
from flask_api import status
from database_wrapper import DatabaseWrapper

class RecommendedMapsResponder():

	def __init__(self, level):
		self._level = level

	def _fetch_recommended_maps(self, level):
		maps = DatabaseWrapper.get_recommended_maps(level)
		return maps

	def get_response(self):
		maps = self._fetch_recommended_maps(self._level)

		return jsonify(maps), status.HTTP_200_OK
