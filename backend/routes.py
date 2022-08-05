from flask import Flask
from maps import RecommendedMapsResponder
from mob import MobResponder

app = Flask(__name__)

@app.route('/recommended_maps/<level>')
def recommended_maps(level):
	responder = RecommendedMapsResponder(level)
	return responder.get_response(), 400

@app.route('/mobs/<map_id>')
def mobs(map_id):
	responder = MobResponder(map_id)
	return responder.get_response(), 400
 
if __name__ == '__main__':
	app.run()
