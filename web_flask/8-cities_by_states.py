#!/usr/bin/python3

"""
Title: Cities by states
Description: Script that starts a Flask web application
@a_idk scripting
"""

from flask import Flask
from flask import render_template
from models import *

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """ method that (handles) teardown db """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ method that displays a HTML page (inside the tag 'BODY') """
    states = storage.all("State").values()
    output = render_template('8-cities_by_states.html', states=states)
    return output


if __name__ == '__main__':
    """ calling the Main """
    app.run(host='0.0.0.0', port=5000)
