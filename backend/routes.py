from flask import Flask
from floask_cors import cross_origin
from recommended_maps_responder import RecommendedMapsResponder
from mobs_responder import MobsResponder

app = Flask(__name__)

@app.route('/recommended_maps/<level>')
def recommended_maps(level):
	responder = RecommendedMapsResponder(level)
	return responder.get_response()

@app.route('/mobs/<map_id>')
def mobs(map_id):
	responder = MobsResponder(map_id)
	return responder.get_response()
 
if __name__ == '__main__':
	app.run()
