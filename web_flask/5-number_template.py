#!/usr/bin/python3
"""This script starts a Flask web application

    Returns:
        Str: Hello HBNB
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def say_Hello():
    """Return a message when starts"""
    return "Hello HBNB!"


@app.route("/hbnb")
def say_HBNB():
    """Return a message"""
    return "HBNB"


@app.route("/c/<text>")
def say_C_text(text):
    """Return a message"""
    txt = text.replace('_', ' ')
    return "C {}".format(txt)


@app.route("/python/")
@app.route("/python/<text>")
def say_python_text(text="is cool"):
    """Return a message"""
    txt = text.replace('_', ' ')
    return "Python {}".format(txt)


@app.route("/number/<int:n>")
def say_is_number(n):
    """Return a message"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def say_HTML_page(n):
    """Return a HTML page"""
    return render_template("5-number.html", number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
