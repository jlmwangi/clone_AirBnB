#!/usr/bin/python3
'''script that starts a flask application'''

from flask import Flask, render_template
from models import storage
from models.state import State
import os


app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
def cities_states():
    states_by_cities = []
    #cities_by_state_list = []

    states = storage.all(State)

    for state in states.values():
        states_by_cities.append({
            'id': state.id,
            'name': state.name,
            'cities': [{'id': city.id, 'name': city.name} for city in state.cities]
        })

    return render_template('8-cities_by_states.html', states=states_by_cities)

@app.teardown_appcontext
def teardown(exception):
    '''remove the current sqlalchemy session'''
    if exception:
        print(f"{exception}")
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
