import json
from flask_api import status

PLACEHOLDER_MAP_NAME_ID1 = {"id": "map_id1", "name": "map_name1"}
PLACEHOLDER_MAP_NAME_ID2 = {"id": "map_id2", "name": "map_name2"}

class RecommendedMapsResponder():

	def __init__(self, level):
		self._level = level

	# TODO: Fetch from DB all maps with (min_level <= level and max_level >= level)
	def _fetch_recommended_maps(self, level):
		return [PLACEHOLDER_MAP_NAME_ID1, PLACEHOLDER_MAP_NAME_ID2]

	def get_response(self):
		maps = self._fetch_recommended_maps(self._level)
		return json.dumps(maps), status.HTTP_200_OK
