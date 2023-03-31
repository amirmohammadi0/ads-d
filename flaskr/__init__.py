import os
from flask import *


def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)
    app.config['UPLOAD_FOLDER'] = os.path.
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # @app.route('/')
    # def index():
    #     return render_template('base.html')

    @app.route('/upload', methods = ['POST'])  
    def upload():  
        if request.method == 'POST':  
            f = request.files['file']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
            return render_template("uploader/Acknowledgement.html", name = f.filename)

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import uploader
    app.register_blueprint(uploader.bp)
    app.add_url_rule('/', endpoint='index')

    return app

