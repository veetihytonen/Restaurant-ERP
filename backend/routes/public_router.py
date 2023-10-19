from flask import request, session, abort
from secrets import token_hex
from flask.blueprints import Blueprint
from services.user_service import UserService
from http import HTTPMethod, HTTPStatus
from utils import check_csrf

def make_public_router(service: UserService) -> Blueprint:
    router = Blueprint("public_router", __name__)
    
    @router.route('/login', methods=[HTTPMethod.POST])
    def login() -> HTTPStatus | tuple[dict, HTTPStatus]:
        request_data = request.get_json()
        username, password = request_data['username'], request_data['password']

        user = service.login(username, password)

        if not user:
            return HTTPStatus.UNAUTHORIZED

        session['user_id'] = user['id']
        session['username'] = user['username']
        session['user_role'] = user['role']
        session['csrf_token'] = token_hex(16)

        return user, HTTPStatus.OK
    
    @router.route('/logout', methods=[HTTPMethod.POST])
    def logout():
        check_csrf()

        del session['user_id']
        del session['username']
        del session['user_role']
        del session['csrf_token']

        return HTTPMethod.OK
    
    @router.route('/register', methods=[HTTPMethod.POST])
    def register() -> tuple[dict, HTTPStatus.CREATED]:
        data = request.get_json()
        username, password, role = data['username'], data['password'], data['role']

        user = service.register(username=username, password=password, role=role)
        
        return user, HTTPStatus.CREATED

    return router
