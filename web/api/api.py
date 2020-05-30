import flask_login
from flask import Blueprint
from flask_login import current_user

bp = Blueprint('test', __name__, url_prefix='/')


@bp.route('/login_not_required', methods=(['GET']))
def login_not_required():
    return {"result": "ok"}


@bp.route('/login_required', methods=(['GET']))
@flask_login.login_required
def login_required():
    return {
        "result": "ok",
        "user_id": current_user.user_id
    }
