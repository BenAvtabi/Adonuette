class Mob():

	def __init__(self, mob_id, name, level, exp):
		self._id = mob_id
		self._name = name
		self._level = level
		self._exp = exp

	def get_dict(self):
		return {"id": self._id,
			"name": self._name,
			"level": self._level,
			"exp": self._exp}
