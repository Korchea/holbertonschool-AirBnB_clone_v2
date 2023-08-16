#!/usr/bin/python3
"""This script starts a Flask web application

    Returns:
        Str: Hello HBNB
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exept):
    """This def terdadown the database"""
    from models import storage
    storage.close()


@app.route("/states_list", strict_slashes=False)
def say_list():
    """Return a HTML page with the lists of States"""
    from models.state import State
    from models import storage
    all_state = storage.all(State)
    sort_dict = sorted(all_state.values(), key=lambda state: state.name)
    return render_template("7-states_list.html", state=sort_dict)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
