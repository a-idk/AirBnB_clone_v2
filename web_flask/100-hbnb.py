#!/usr/bin/python3

"""
Title: HBNB is alive!
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


@app.route('/hbnb', strict_slashes=False)
def hbnb_alive():
    """ method that main HBNB page """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    output = render_template(
            '100-hbnb.html', states=states, amenities=amenities, places=places
            )
    return output


if __name__ == '__main__':
    """ calling the Main """
    app.run(host='0.0.0.0', port=5000)
