#!/usr/bin/python3

"""
Title: HBNB filters
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


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """display a HTML page like 6-index.html from static"""
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    output = render_template(
            '10-hbnb_filters.html', states=states, amenities=amenities
            )
    return output


if __name__ == '__main__':
    """ calling the Main """
    app.run(host='0.0.0.0', port=5000)
