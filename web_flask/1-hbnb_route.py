#!/usr/bin/python3
"""
Title: HBNB
Description: Script that starts a Flask application
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
