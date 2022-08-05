from flask import Flask
import Mob

app = Flask(__name__)

@app.route('/maps/<level>')
def maps(level):
    responder = MapsResponder(level)
    return responder.get_response(), 400

@app.route('/mob/<id>')
def mob(id):
	responder = MobResponder(id)
    return responder.get_response(), 400
 
if __name__ == '__main__':
    app.run()
