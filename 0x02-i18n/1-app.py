#!/usr/bin/env python3
""" A flask template that supports babel"""


from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """ The config class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFUALT_TIMEZONE = 'UTC'


# flask app configurations
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """ the index function """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
