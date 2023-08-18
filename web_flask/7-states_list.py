from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def rot7(excepetion):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def lista():
    state = storage.all(State).values()
    return render_template('7-states_list.html', state=state)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
