import json
from mob import Mob


class DatabaseWrapper:

	# TODO: actually fetch from db
	@classmethod
	def get_mob_by_id(cls, mob_id):
		MOB_NAME_PLACEHOLDER = "testMob"
		MOB_LEVEL_PLACEHOLDER = 275
		MOB_EXP_PLACEHOLDER = 10
		dummy_mob = Mob(mob_id, MOB_NAME_PLACEHOLDER, MOB_LEVEL_PLACEHOLDER, MOB_EXP_PLACEHOLDER)

		return dummy_mob

	# TODO: actually fetch from db
	@classmethod
	def get_mobs_in_map(cls, map_id):	
		PLACEHOLDER_MOB_IDS = [0, 1]
		return PLACEHOLDER_MOB_IDS

	# TODO: Fetch from DB all maps with (min_level <= level and max_level >= level)
	@classmethod
	def get_recommended_maps(cls, level):
		PLACEHOLDER_MAP_NAME_ID1 = {"id": "map_id1", "name": "map_name1"}
		PLACEHOLDER_MAP_NAME_ID2 = {"id": "map_id2", "name": "map_name2"}
		return [PLACEHOLDER_MAP_NAME_ID1, PLACEHOLDER_MAP_NAME_ID2]