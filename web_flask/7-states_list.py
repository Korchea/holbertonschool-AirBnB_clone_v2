#!/usr/bin/python3
"""This script starts a Flask web application

    Returns:
        Str: Hello HBNB
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown():
    """This def terdadown the database"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def say_list():
    """Return a HTML page with the lists of States"""
    state = storage.all(State)
    sort_dict = dict(sorted(state.items(), key=lambda item: item[1]))
    return render_template("7-states_list.html", tables="States", states=sort_dict)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
