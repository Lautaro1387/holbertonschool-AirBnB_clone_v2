#!/usr/bin/python3
"""Script that starts a Flask web application"""


from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def storage(exception):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all(State)
    all_st = []

    for state in states.values():
        all_st.append([state.id, state.name])
    return render_template('7-states_list.html', states=all_st)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
