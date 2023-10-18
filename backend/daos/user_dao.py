from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import text

class IngredientDao:

    def __init__(self, db_connection: SQLAlchemy) -> None:
        self.__db = db_connection

    def create_user(username: str, password: str):
