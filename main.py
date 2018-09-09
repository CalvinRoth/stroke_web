import firebase_admin
from firebase_admin import credentials

from flask import Flask, request
from flask_restful import Api

from resources.recognize import Recognizer

cred = credentials.Certificate("./ServiceAccountKey.json")
firebase_admin.initialize_app(cred)

app = Flask(__name__)
api = Api(app)

api.add_resource(Recognizer, '/recognize')

if __name__ == '__main__':
	app.run(debug=True)

# app.run(host='0.0.0.0', port=80)
