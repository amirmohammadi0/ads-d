from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app
)
from werkzeug.exceptions import abort
import os
from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('uploader', __name__)


@bp.route('/')
def index():
    return render_template('uploader/index.html')


# @bp.route('/upload', methods = ['POST'])  
# def upload():  
#     if request.method == 'POST':  
#         f = request.files['file']
#         f.save(os.path.join(current_app.config['UPLOAD_FOLDER'], f.filename))
#         return render_template("uploader/Acknowledgement.html", name = f.filename)