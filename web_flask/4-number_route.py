#!/usr/bin/python3
"""
Title: Python is cool!
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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_cool(text='is cool'):
    """
    method that display “Python ”, followed by the value of the
    text variable
    """
    output = 'Python ' + text.replace('_', ' ')
    return output


@app.route('/number/<int:n>', strict_slashes=False)
def d_number(n):
    """ method that display “n is a number” only if n is an integer
    """
    output = f"{n:d} is a number"
    return output


if __name__ == '__main__':
    """ Call from Main """
    app.run(host='0.0.0.0', port='5000')
