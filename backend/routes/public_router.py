from flask import request
from flask.blueprints import Blueprint

from http import HTTPMethod, HTTPStatus


def make_public_router() -> Blueprint:
    router = Blueprint("public_router", __name__)
    
    @router.route('/login', methods=[HTTPMethod.POST])
    def login():
        data = request.get_json()
        username, password, role = data['username'], data['password'], data['role']
        

    
    return router
