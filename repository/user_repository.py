from model.user import User

# Use global variables as a Database.
user_store = []

class UserRepository(object):

    @staticmethod
    def insert(user: User) -> None:
        user_store.append(user)

    @staticmethod
    def get_by_id(user_id: str) -> User:
        match = list(filter(
            lambda x: x.user_id == user_id,
            user_store)
        )
        if len(match) != 1:
            return None
        return match[0]