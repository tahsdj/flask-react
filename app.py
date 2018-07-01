from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={"/api/*": {"origins": "*"}})

@app.route('/api/', methods=['GET'])

def index_page():
	resObj = {
		'content': 'Hello, flask-react'
	}
	return jsonify(resObj)

app.run(port=5000, debug=True)