#!/usr/bin/python3
"""Start Flask web app"""


from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__, template_folder="templates")


@app.teardown_appcontext
def db_close():
    storage.close()


@app.route("/", strict_slashes=False)
def hello():
    """great the best school"""

    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """best school page"""

    return "HBNB!"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """extract url text and append to `C `"""

    return f"C {text.replace('_', ' ')}"


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>")
def python_route(text):
    """extract defaulted url text and append to `Python `"""

    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """
    - extract url text and prepend to ` is a number`
    - dependent on text url being an `int` typed digit
    """

    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template_route(n):
    """renders template with given integer"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_is_odd_or_even_template_route(n):
    """
    renders HTML template stating if given url integer
    is odd or even
    """

    template = "6-number_odd_or_even.html"
    odd_or_even = f"{n} is odd" if n % 2 else f"{n} is even"
    return render_template(template, odd_or_even=odd_or_even)


@app.route("/states_list", strict_slashes=False)
def states_list_route():
    """order list of states in storage"""

    template = "7-states_list.html"
    h1_tag= "States"

    key = lambda x: x.name

    states = storage.all("States").values()
    states = [state for state in sorted(states, key=key)]

    return render_template(template, h1_tag=h1_tag, states=states)


if __name__ == "__main__":
    print(storage.all())
    app.run(host="0.0.0.0", port=5000)
