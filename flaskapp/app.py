from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_sqlalchemy import SQLAlchemy
from data import Configurations
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

app = Flask(__name__)

# postgres
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///envecho'
# debug
app.debug = True
db = SQLAlchemy(app)

Configurations = Configurations()

# postgres


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))

    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r' % self.username


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
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.hash(str(form.password.data))

        user = Users(request.form['name'], request.form['username'], request.form['email'],
                     request.form[password])
        db.session.add(user)
        db.session.commit()

        return render_template('register.html', form=form)
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run()
