from daos.user_dao import UserDao

class UserService:
    def __init__(self, dao: UserDao) -> None:
        self.__dao = dao

    def login(self, username: str, password: str) -> bool | dict:
        results = self.__dao.login(username, password)
        
        if not results:
            return False
        
        for_json = {'id': results[0], 'username': results[1], 'role': results[2]}

        return for_json

    def register(self, username: str, password: str, role: int) -> tuple:
        user_id, username, role  = self.__dao.create_user(username, password, role)

        for_json = { 'id': user_id, 'username': username, 'role': role }

        return for_json
