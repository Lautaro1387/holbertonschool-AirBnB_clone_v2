#!/usr/bin/python3
"""Script that starts a web application"""

from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.teardown_appcontext
def closed(self):
    from models import storage
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    from models import storage
    from models.state import State
    """display a HTML page: (inside the tag BODY)"""
    closed = storage.all(State).values()
    return render_template('7-states_list.html', states=context)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    from models.city import City
    from models.state import State
    from models import storage
    """DBStorage in order"""
    city_obj = {
        'states': storage.all(State).values(),
        'cities': storage.all(City).values()
    }

    return render_template('8-cities_by_states.html', **city_obj)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
