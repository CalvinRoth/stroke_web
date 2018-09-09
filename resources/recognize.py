from flask import current_app, request
from flask_restful import Resource
import os
import base64
from werkzeug.utils import secure_filename
from firebase_admin import firestore

class Recognizer(Resource):
    def __init__(self):
        self.db = firestore.client()
    def get(self):
        return {'message': 'hello'}
    def post(self):
        # file =request.files['files']
        body = request.get_json()
        image = body['image']

        with open("testImage.png", "wb") as fh:
            fh.write(base64.decodebytes(image.encode('ascii')))

        # if file and allowed_file(file.filename):
        #     filename = secure_filename(file.filename)
        #     file.save(os.path, join(app.config['UPLOAD_FOLDER'], filename))
        #     return
        return {'message': image}
        # img = open(img_file, 'rb').read()
        # response = requests.post(URL, data=img, headers=headers)
        # return response
        # doc_ref = self.db.collection('sampleData').document('faces')
        # doc_ref.set({
        #     'eyes': 123,
        #     'mouth': 321
        # })
        # return {'message': 'Hello there'}
