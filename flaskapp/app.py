from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from data import Configurations
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from database import Database

app = Flask(__name__)

Configurations = Configurations()
db = Database()


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/configurations')
def configurations():
    return render_template('configurations.html', configurations=Configurations)


@app.route('/configuration/<string:id>/')
def configuration(id):
    return render_template('configuration.html', id=id)


class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [validators.DataRequired(
    ), validators.EqualTo('confirm', message='invalid credentials')])
    confirm = PasswordField('Confirm Password')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        return render_template('register.html')
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run()
