import os

import firebase_admin
import flask_login
from firebase_admin import credentials
from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=False)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    login_manager = flask_login.LoginManager()
    login_manager.init_app(app)
    from web.helper.auth import request_loader, unauthorized_handler
    login_manager.request_loader(request_loader)
    login_manager.unauthorized_handler(unauthorized_handler)

    # Initialize Firebase Admin
    cred = credentials.Certificate('PATH_TO_SERVICE_ACCOUNT.json')
    firebase_admin.initialize_app(cred)

    from .api import api
    app.register_blueprint(api.bp)


    return app
