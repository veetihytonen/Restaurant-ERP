from flask import request, session, abort

def check_csrf():
    if session['csrf_token'] != request.form['csrf_token']:
        abort(403)
