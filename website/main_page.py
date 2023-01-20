# import os
# from flask import Flask, flash, request, redirect, url_for
# from werkzeug.utils import secure_filename

# UPLOAD_FOLDER = '/path/to/the/uploads'
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

import re
from datetime import datetime

from flask import Flask, render_template
import flask
app = Flask(__name__)
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'upload_direction/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/')  
def main():  
    return render_template("index.html")  
  
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']
        basedir = os.path.abspath(os.path.dirname(__file__))
        f.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], f.filename))
        return render_template("Acknowledgement.html", name = f.filename)  

# @app.route('/select_page', methods = ['GET'])  
# def select_page():  
#     if request.method == 'GET':  
#         return render_template("select_page.html")  

@app.route('/select_page', methods = ['GET'])    
def select_page():
    images = os.listdir(os.path.join(app.static_folder, "images"))
    print("ZOOOO")
    # print(images)
    return render_template('select_page.html',images=images)
if __name__ == "__main__":
    app.run(debug=True)