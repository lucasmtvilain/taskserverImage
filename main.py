import os
import ConvertImage
import urllib.request
from app import app
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

#retourne le nom du fichier s'il possède une extension autorisé
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods = ['GET', 'POST'])
def index():
    return '{"title": "The Basics - Networking","description": "Your app fetched this from a remote endpoint!","movies": [{ "id":"1", "title": "l\'api fonctionne","releaseYear": "!" }]}'
# Upload des fichier
@app.route('/file-upload', methods=['POST'])
def upload_file():
    print(request.files)
	# check if the post request has the file part
    if 'file' not in request.files:
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp
    file = request.files['file']

    if file.filename == '':
        resp = jsonify({'message' : 'No file selected for uploading'})
        resp.status_code = 400
        return resp

    #si le fichier et l'extension sont ok
    if file and allowed_file(file.filename):
        #recuperation du nom du fichier uploade
        filename = secure_filename(file.filename)
        #URL du fichier sur le server
        fileURL = app.config['UPLOAD_FOLDER']+'/'+file.filename
        print(fileURL)
        #on enregistre l'image sur le server
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #reponse au client
        resp = jsonify({'message' : 'File successfully uploaded'})
        #status code
        resp.status_code = 201

        # URL du fichier sur le server
        fileURL = app.config['UPLOAD_FOLDER'] + '/' + file.filename
        print(fileURL)
        ConvertImage.convert_file(fileURL)
        return resp

    else:
        #resultat en cas d'erreur
        resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
        resp.status_code = 400
        return resp

if __name__ == "__main__":
    # !!!!! Mettre l'ip du raspberry !!!!!!!!!!!!!
    #app.run(host="192.168.1.25", port="5000")
    app.run()