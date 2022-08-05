import json
from flask_api import status

MOB_ID_PLACEHOLDER = 69
MOB_NAME_PLACEHOLDER = "testMob"
MOB_LEVEL_PLACEHOLDER = 275
MOB_EXP_PLACEHOLDER = 10


MAP_ID_PLACEHOLDER = 420
MAP_NAME_PLACEHOLDER = "testMap"
MAP_MOBS_PLACEHOLDER = [0, 1]

class Map():

	def __init__(self, map_id, name, mobs):
		self._id = map_id
		self._name = name
		self._mobs = mobs

	def get_dict(self):
		map_dict = {"name": self._name, "mobs": self._mobs}
		return map_dict

	@classmethod
	def create_dummy(cls, id=MAP_ID_PLACEHOLDER):
		return Map(id, MAP_NAME_PLACEHOLDER, MAP_MOBS_PLACEHOLDER)

	def get_id(self):
		return self._id

	def get_mobs(self):
		return self._mobs

class Mob():

	def __init__(self, mob_id, name, level, exp):
		self._id = mob_id
		self._name = name
		self._level = level
		self._exp = exp

	@classmethod
	def create_dummy(cls, mob_id=MOB_ID_PLACEHOLDER):
		return Mob(mob_id, MOB_NAME_PLACEHOLDER, MOB_LEVEL_PLACEHOLDER, MOB_EXP_PLACEHOLDER)

	def get_dict(self):
		return {"name": self._name,
			"level": self._level,
			"exp": self._exp}

	def get_id(self):
		return self._id


class MobResponder():

	def __init__(self, map_id):
		self._map_id = map_id

	# TODO: Fetch mob_ids by map id from DB
	def _fetch_mob_ids(self, map_id):
		map = Map.create_dummy(map_id)
		mob_ids = map.get_mobs()
		return mob_ids

	# TODO: Fetch mob by id from DB
	def _fetch_mob(self, mob_id):
		return Mob.create_dummy(mob_id)

	def get_response(self):
		mob_ids = self._fetch_mob_ids(self._map_id)
		mobs = [self._fetch_mob(mob_id) for mob_id in mob_ids]
		mobs_dict = {mob.get_id(): mob.get_dict() for mob in mobs}

		return json.dumps(mobs_dict), status.HTTP_200_OK
