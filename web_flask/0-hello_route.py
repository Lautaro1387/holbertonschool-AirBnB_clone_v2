#!/usr/bin/python3
""" Script that starts Flask web application
    Return: Hello HBNB!
"""


from flask import Flask


app = Flask(__name__)
@app.route('/', strict_slashes=False)
def hello():
    return f'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
