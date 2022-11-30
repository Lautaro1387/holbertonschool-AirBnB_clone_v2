#!/usr/bin/python3
""" Script that starts Flask web application
    Return: Hello HBNB!
            HBNB
            C is cool
            Python is cool
            <int> is a number
            Number: <n>
            Number: <n> is even|odd
"""


from flask import Flask, render_template
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


@app.route('/python', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    return 'Python {}'.format(escape(text).replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '{} is a number'.format(escape(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
