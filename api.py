import covid_classification as cc
import flask
import os
import cv2
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin

UPLOAD_FOLDER =  'static/images/original'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
PREPROCESS_FOLDER = 'static/images/testing'

app = flask.Flask(__name__)
app.secret_key = "1234zzzz"
app.config["DEBUG"] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PREPROCESS_FOLDER'] = PREPROCESS_FOLDER

CORS(app, origin='*')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/predict', methods=['GET','POST'])
def process():
    if request.method == 'GET':
        placeholder = 'static/img/default-placeholder.png'
        return render_template('classification.html', 
                                img_url=placeholder, 
                                img_processed=placeholder, 
                                prediction='Result')

    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Please choose a picture')
            return redirect(request.url)

        image = request.files.get('file')
        mode = request.form.get('mode')
        if image.filename == "":
            flash('Please choose a picture')
            return redirect(request.url)

        if mode is None:
            mode = 'none'
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(filepath)
            pred, prob, img_processed = cc.predict(filepath, mode)
            result = str(pred) + ' ' + str(round(prob*100)) + '%'
            img_processed_path = os.path.join(app.config['PREPROCESS_FOLDER'], mode, filename)
            cv2.imwrite(img_processed_path, img_processed)

        return render_template('classification.html',
                                img_url=filepath, 
                                img_processed=img_processed_path, 
                                prediction=result)

app.run()