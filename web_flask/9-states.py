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


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """ method display the states and cities """
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    op = render_template('9-states.html', states=states, state_id=state_id)
    return op


if __name__ == '__main__':
    """ calling the Main """
    app.run(host='0.0.0.0', port=5000)
