from flask import render_template, request, redirect, \
     url_for, flash, abort
from flask_login import login_user, logout_user, login_required

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm

@app.route('/auth/login', methods = ['GET', 'POST'])
def auth_login():
    if request.method == 'GET':
        return render_template('auth/loginform.html', form = LoginForm())

    form = LoginForm(request.form)
    # for possible validations

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template('auth/loginform.html', form = form,
        error = 'Väärä käyttäjätunnus tai salasana')

    login_user(user)
    flash('Kirjautuminen onnistui')

    # TODO
    #next = flask.request.args.get('next')
    # is_safe_url should check if the url is safe for redirects.
    # See http://flask.pocoo.org/snippets/62/ for an example.
    #if not is_safe_url(next):
    #    return flask.abort(400)

    return redirect(url_for('index'))

@app.route('/auth/logout')
@login_required
def auth_logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods = ['GET', 'POST'])
def user_register():
    if request.method == 'GET':
        return render_template('auth/register.html', form = RegisterForm())

    form = RegisterForm(request.form)

    if not form.validate():
        return render_template('auth/register.html', form = form)

    name = form.name.data
    username = form.username.data
    password = form.password.data

    user = User(name, username, password)

    db.session().add(user)
    db.session().commit()

    return render_template('auth/loginform.html', form = LoginForm())
