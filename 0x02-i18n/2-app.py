#!/usr/bin/env python3
""" a simple flask app with babel localeselector """


from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ a configuration class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCAL = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# configure the flask app
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel_localeselector
def get_locale():
    """ a method to accept the supported languages """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ an index function """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
