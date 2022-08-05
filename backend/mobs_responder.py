import json
from flask_api import status
from database_wrapper import DatabaseWrapper

class MobsResponder():

	def __init__(self, map_id):
		self._map_id = map_id

	def _fetch_mob_ids(self, map_id):
		mob_ids = DatabaseWrapper.get_mobs_in_map(map_id)
		return mob_ids

	def _fetch_mob(self, mob_id):
		mob = DatabaseWrapper.get_mob_by_id(mob_id)
		return mob

	def get_response(self):
		mob_ids = self._fetch_mob_ids(self._map_id)
		mobs = [self._fetch_mob(mob_id).get_dict() for mob_id in mob_ids]

		return json.dumps(mobs), status.HTTP_200_OK
