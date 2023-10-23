from flask import request, session, render_template, redirect, flash, Response
from flask.blueprints import Blueprint
from services.ingredient_service import IngredientService
from utils import check_csrf, check_auth
from http import HTTPMethod

def make_ingredient_router(service: IngredientService) -> Blueprint:
    router = Blueprint('ingredient_router', __name__)

    @router.route('/', methods=[HTTPMethod.GET])
    def get_ingredients():
        auth = check_auth(access_level=1)
        if not auth[0]:
            return auth[1]

        ingredients = service.get_all()

        return render_template('ingredients.html', ingredients=(ingredients))

    @router.route('/', methods=[HTTPMethod.POST])
    def create_ingredient():
        auth = check_auth(access_level=1)
        if not auth[0]:
            return auth[1]

        check_csrf()

        name, category = request.form['name'], request.form['category']
        
        try:
            result = service.create(name=name, category=category)
        except ValueError as ve:
            flash(ve.args[0], 'error')
            return redirect('/ingredients')

        flash(f'Luotiin raaka-aine "{name}"', 'notification')
        return redirect('/ingredients')
    
    return router
