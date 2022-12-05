#!/usr/bin/python3
"""Script that starts a Flask web application"""


from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def storage_close(self):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    storage_close = storage.all(State).values()
    return render_template('7-states_list.html', states=storage_close)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    city_obj = {
        'states' = storage.all(State).values()
        'cities' = storage.all(City).values()
    }
    return render_template('8-cities_by_states.html', city_obj)
