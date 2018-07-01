from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index_page():
	return 'hello world'

app.run(port=5000, debug=True)