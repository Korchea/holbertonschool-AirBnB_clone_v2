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


@app.route('/states', strict_slashes=False)
def lista():
    state = storage.all(State).values()
    return render_template('7-states_list.html', state=state)


@app.route('/states/<id>', strict_slashes=False)
def say_state_id(id):
    """Return a HTML page with the lists of States with the same id"""
    states = storage.all(State).values()
    id_aux = "NF"
    for state in states:
        if state.id == id:
            id_aux = id
            break
    return render_template("9-states.html", state=state, id_aux=id_aux)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
