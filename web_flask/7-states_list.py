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
def teardown(exept):
    """This def terdadown the database"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Return a HTML page with the lists of States"""
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


"""@app.route("/states_list", strict_slashes=False)
def say_list():
    
    all_state = storage.all(State)
    sort_dict = sorted(all_state.values(), key=lambda state: state.name)
    return render_template("7-states_list.html", state=sort_dict)
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
