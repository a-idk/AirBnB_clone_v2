#!/usr/bin/python3

"""
Title: List of states
Description: Script that starts a Flask web application
@a_idk scripting
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """ method that (handles) teardown db """
    if storage is not None:
        storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ method that displays a HTML page (inside the tag 'BODY') """
    info = storage.all(State)
    output = render_template('7-states_list.html', total=info.values())
    return output


if __name__ == '__main__':
    """ calling the Main """
    app.run(host='0.0.0.0', port=5000)
