from firebase_admin import auth
from firebase_admin.auth import InvalidIdTokenError

from model.user import User
from repository.user_repository import UserRepository


def request_loader(request):
    user_token = request.headers.get('X-Auth-Token')
    if user_token is None:
        return

    try:
        # https://firebase.google.com/docs/auth/admin/verify-id-tokens?hl=ja#verify_id_tokens_using_the_firebase_admin_sdk
        firebase_auth_info = auth.verify_id_token(user_token)
    except InvalidIdTokenError:
        return

    user_id = firebase_auth_info['uid']
    repository = UserRepository()
    stored_user = repository.get_by_id(user_id)
    if stored_user is not None:
        return stored_user

    # Register DB a new user.
    new_user = User(
        user_id=user_id
    )
    repository.insert(new_user)
    return new_user


def unauthorized_handler():
    return {"result": "unauthorized"}, 401
