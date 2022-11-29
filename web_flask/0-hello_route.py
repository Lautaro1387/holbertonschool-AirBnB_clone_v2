#!/usr/bin/python3
"""Script"""
from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return f'Hello HBNB!'

if __name__ == '__main__':
    app.run(strict_slashes=False, port=5000)