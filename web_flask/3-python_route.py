#!/usr/bin/python3
""" Script that starts Flask web application
    Return: Hello HBNB!, HBNB
"""


from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return 'C {}'.format(escape(text).replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False, defaults={text: 'is cool'})
def python_text(text):
    return 'Python {}'.format(escape(text).replace('_', ' '))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
