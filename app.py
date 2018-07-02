from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={"/api/*": {"origins": "*"}})

@app.route('/', methods=['GET'])
def hello_flask():
	return 'hello flask'


@app.route('/api/hello-world', methods=['GET'])
def say_hello():
	resObj = {
		'content': 'Hello, flask-react'
	}
	return jsonify(resObj)

app.run(host='0.0.0.0', port=80)