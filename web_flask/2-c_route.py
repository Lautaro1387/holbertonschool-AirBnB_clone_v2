#!/usr/bin/python3
""" Script that starts Flask web application
    Return: Hello HBNB!, HBNB
"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text():
    return 'C {(text)}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
