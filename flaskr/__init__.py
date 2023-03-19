import os
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        # بعدا کاملش میکنم
    )
    try:
        os.mkdir(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return "hello world"
    
    from . import db
    db.init_app(app)

    return app

create_app().run(host='localhost')