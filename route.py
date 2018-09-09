import os
from flask import Flask, request
from werkzeug.utils import secure_filename
from main import app

UPLOAD_FOLDER = '../'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods = ['GET', 'POST'])
def uploadImage():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash("No file part")
            return {'message': 'Error: Incomplete request'}
        file = request.files['files']
        if file.filename == '':
            flash('No selected file')
            return {'message': 'Error: File name is empty'}
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('../', filename))
            #algo
    return {'message': 'Hello there'}
