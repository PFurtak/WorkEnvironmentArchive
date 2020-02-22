from flask import Flask, render_template
from data import Configurations

app = Flask(__name__)

Configurations = Configurations()


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


if __name__ == '__main__':
    app.run()
