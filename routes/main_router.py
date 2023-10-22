from flask import request, session, render_template, redirect, flash
from flask.blueprints import Blueprint
from services.user_service import UserService
from http import HTTPMethod, HTTPStatus
from utils import check_csrf

def make_main_router(service: UserService) -> Blueprint:
    router = Blueprint("main_router", __name__)

    @router.route('/', methods=[HTTPMethod.GET])
    def home():
        if 'username' in session:
            return render_template('index.html')
        else:
            return redirect('/login')

    @router.route('/login', methods=[HTTPMethod.GET])
    def login_page():
        return render_template('login.html')
    
    @router.route('/login', methods=[HTTPMethod.POST])
    def login_action():
        username = request.form['username']
        password = request.form['password']

        user = service.login(username, password)

        if not user:
            flash('Väärä tunnus tai salasana')
            return redirect('/login')        
        
        return redirect("/")
    
    @router.route('/logout', methods=[HTTPMethod.GET])
    def logout():
        del session['user_id']
        del session['username']
        del session['user_role']
        del session['csrf_token']

        return redirect('/login')
    
    @router.route('/register', methods=[HTTPMethod.GET])
    def register_page():
        return render_template('register.html')

    @router.route('/register', methods=[HTTPMethod.POST])
    def register_action():
        form = request.form
        username, passw1, passw2, role = form['username'], form['password1'], form['password2'], form['role'], 
        
        try:
            user = service.register(username=username, password1=passw1, password2=passw2, role=role)
        except ValueError as ve:
            flash(ve.args[0])
            return redirect('/register')
        
        flash('Käyttäjän luominen onnistui')
        return redirect('/login')

    return router
