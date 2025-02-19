#!/usr/bin/python3
"""This script starts a Flask web application

    Returns:
        Str: Hello HBNB
"""
from flask import Flask, render_template
from models.state import State
from models.city import City
from models.amenity import Amenity
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exeption):
    """This def terdadown the database"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def dis_index():
    """Display a HTML page like 6-index.html, which was done during the
    project 0x01. AirBnB clone - Web static"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
