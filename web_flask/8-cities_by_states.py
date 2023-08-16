#!/usr/bin/python3
"""This script starts a Flask web application

    Returns:
        Str: Hello HBNB
"""
from flask import Flask, render_template
from models.state import State
from models.city import City
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exeption):
    """This def terdadown the database"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def say_list():
    """Return a HTML page with the lists of States"""
    state = storage.all(State)
    return render_template("8-cities_by_states.html", states=state)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
