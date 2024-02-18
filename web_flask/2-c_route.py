#!/usr/bin/python3
"""
Title: C is fun
Description: Script that starts a Flask application
@a_idk scripting
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ method that returns Hello HBNB! """
    output = 'Hello HBNB!'
    return output


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ method that returns 'HBNB' """
    output = 'HBNB'
    return output


@app.route('/c/<text>', strict_slashes=False)
def c_Fun(text):
    """
    method that display “C ” followed by the value of the text
    variable (replace underscore _ symbols with a space
    """
    output = "C " + text.replace('_', ' ')
    return output


if __name__ == '__main__':
    """ Call from Main """
    app.run(host='0.0.0.0', port='5000')
