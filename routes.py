from flask import Flask

app = Flask(__name__)

@app.route('/maps/<level>')
def maps(level):
    return 0, 400

@app.route('/mob/<id>')
def maps(id):
    return 0, 400
 
if __name__ == '__main__':
    app.run()