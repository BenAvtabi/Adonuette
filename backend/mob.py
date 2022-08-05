import json

MOB_ID_PLACEHOLDER = 69
MOB_NAME_PLACEHOLDER = "testMob"
MOB_LEVEL_PLACEHOLDER = 275
MOB_EXP_PLACEHOLDER = 10


class Mob():

	def __init__(self, mob_id, name, level, exp):
		self._id = mob_id
		self._name = name
		self._level = level
		self._exp = exp

	@classmethod
	def create_dummy(cls):
		return Mob(MOB_ID_PLACEHOLDER, MOB_NAME_PLACEHOLDER, MOB_LEVEL_PLACEHOLDER, MOB_EXP_PLACEHOLDER)

	def get_dict(self):
		return {"name": self._name,
			"level": self._level,
			"exp": self._exp}

	def get_id(self):
		return self._id


class MobResponder():

	def __init__(self, mob_id):
		self._id = mob_id

	# TODO: Fetch from DB
	def _fetch_mob(self, mob_id):
		return Mob.create_dummy()

	def get_response(self):
		mob = self._fetch_mob(self._id)
		return json.dumps(mob.get_dict())
