import json
import Mob

MAP_ID_PLACEHOLDER = 420
MAP_NAME_PLACEHOLDER = "testMap"

class Map():

	def __init__(map_id, name, mobs):
		self._id = map_id
		self._name = name
		self._mobs = mobs

	def get_dict(self):
		mobs_dict = {mob.get_id(): mob.get_dict() for mob in self._mobs}
		map_dict = {"name": self._name, "mobs": mobs_dict}
		return map_dict

	@classmethod
	def create_dummy(cls):
		return Map(MAP_ID_PLACEHOLDER, MAP_NAME_PLACEHOLDER, [Mob.create_dummy()])

	def get_id(self):
		return self._id

class MapsResponder():

	def __init__(self, level):
		self._level = level

	# TODO: Fetch from DB all maps with (min_level <= level and max_level >= level)
	def _fetch_maps(level):
		return [Map.create_dummy(), Map.create_dummy()]

	def get_response(self):
		maps = self._fetch_maps(self._level)
		map_dict = {map.get_id(): map.get_dict() for map in maps}
		return json.dump(map_dict)
