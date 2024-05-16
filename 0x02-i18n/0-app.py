#! /usr/bin/env python3
""" A simple flask application """


from flask import Falsk, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    """ default hello world route """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(port="5000", hosst="0.0.0.0", debug="True")
