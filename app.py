import fileinput

from flask import Flask
from flask import flash
from flask import Blueprint
from flask import request, render_template, redirect, url_for
from fruuty_token.fruuty_token import fruuty_token_bp
from fruuty_player.fruuty_player import fruuty_player_bp

"""
File uploads import section
"""

import os
from werkzeug.utils import secure_filename
from flask import send_from_directory

UPLOAD_FOLDER = 'fruuty_token/static/img/'
ALLOWED_EXTENSIONS = { 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'wav', 'mp3'}

app = Flask(__name__)


"""
Config settings
"""
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'the random string'

"""
Blueprint registration section
"""
app.register_blueprint(fruuty_token_bp)
app.register_blueprint(fruuty_player_bp)

"""
main app config routes section
"""

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/music-upload', methods=['GET', 'POST'])
def music_upload():
    if request.method == 'POST':
        #check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect((request.url))
        file_to_upload = request.files['file']
        # if the usr does not select a file, the browser submits an
        # empty file without a filename.

        if file_to_upload.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file_to_upload and allowed_file(file_to_upload.filename):
            filename = secure_filename(file_to_upload.filename)
            file_to_upload.save(os.path.join(app.config['UPLOAD_FOLDER'] + 'music', filename))
            return render_template('message.html')
    return render_template('music_upload.html')

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config['UPLOAD_FOLDER'] + 'music', name)



"""
food upload route section
"""

@app.route('/food-upload', methods=['GET', 'POST'])
def food_upload():
    if request.method == 'POST':
        #check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect((request.url))
        file_to_upload = request.files['file']
        # if the usr does not select a file, the browser submits an
        # empty file without a filename.

        if file_to_upload.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file_to_upload and allowed_file(file_to_upload.filename):
            filename = secure_filename(file_to_upload.filename)
            file_to_upload.save(os.path.join(app.config['UPLOAD_FOLDER'] + 'food', filename))
            return redirect(url_for('download_food', name=filename))
    return render_template('file_upload.html')

@app.route('/uploads/<name>')
def download_food(name):
    return send_from_directory(app.config['UPLOAD_FOLDER'] + 'food', name)




"""
fashion upload route section
"""

@app.route('/fashion-upload', methods=['GET', 'POST'])
def fashion_upload():
    if request.method == 'POST':
        #check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect((request.url))
        file_to_upload = request.files['file']
        # if the usr does not select a file, the browser submits an
        # empty file without a filename.

        if file_to_upload.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file_to_upload and allowed_file(file_to_upload.filename):
            filename = secure_filename(file_to_upload.filename)
            file_to_upload.save(os.path.join(app.config['UPLOAD_FOLDER'] + 'fashion', filename))
            return redirect(url_for('download_fashion', name=filename))
    return render_template('fashion_upload.html')

@app.route('/uploads/<name>')
def download_fashion(name):
    return send_from_directory(app.config['UPLOAD_FOLDER'] + 'fashion', name)




"""
drive upload route section
"""

@app.route('/drive-upload', methods=['GET', 'POST'])
def drive_upload():
    if request.method == 'POST':
        #check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect((request.url))
        file_to_upload = request.files['file']
        # if the usr does not select a file, the browser submits an
        # empty file without a filename.

        if file_to_upload.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file_to_upload and allowed_file(file_to_upload.filename):
            filename = secure_filename(file_to_upload.filename)
            file_to_upload.save(os.path.join(app.config['UPLOAD_FOLDER'] + 'drive', filename))
            return redirect(url_for('download_drive', name=filename))
    return render_template('drive_upload.html')

@app.route('/uploads/<name>')
def download_drive(name):
    return send_from_directory(app.config['UPLOAD_FOLDER'] + 'drive', name)



"""
drive upload route section
"""

@app.route('/smart-tech-upload', methods=['GET', 'POST'])
def smart_tech_upload():
    if request.method == 'POST':
        #check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect((request.url))
        file_to_upload = request.files['file']
        # if the usr does not select a file, the browser submits an
        # empty file without a filename.

        if file_to_upload.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file_to_upload and allowed_file(file_to_upload.filename):
            filename = secure_filename(file_to_upload.filename)
            file_to_upload.save(os.path.join(app.config['UPLOAD_FOLDER'] + 'smart_tech', filename))
            return redirect(url_for('download_smart_tech', name=filename))
    return render_template('smart_tech_upload.html')


@app.route('/uploads/<name>')
def download_smart_tech(name):
    return send_from_directory(app.config['UPLOAD_FOLDER'] + 'smart_tech', name)



if __name__ == '__main__':
    app.run(debug=True)


