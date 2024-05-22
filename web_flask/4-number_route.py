#!/usr/bin/python3
"""Start Flask web app"""


from flask import Flask
app = Flask(__name__)


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
def int_route(n):
    """
    - extract url text and prepend to ` is a number`
    - dependent on text url being an `int` typed digit
    """

    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
