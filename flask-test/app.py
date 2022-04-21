from urllib import request
from flask import Flask, request, response,  jsonify

#Creation of an Flask app instance 
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'First Api Calling'


@app.route('/post', methods=["POST"])
def post_testing():
    input_json = request.get_json(force=True)
    dictToReturn = {'text': input_json['text']}
    return jsonify(dictToReturn)
