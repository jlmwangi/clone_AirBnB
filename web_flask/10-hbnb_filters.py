#!/usr/bin/python3
'''script that starts a flask application'''

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
import os


app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    states_by_cities = []
    amenities_list = []

    states = storage.all(State)
    amenities = storage.all(Amenity)

    for state in states.values():
        states_by_cities.append({
            'id': state.id,
            'name': state.name,
            'cities': [{'id': city.id, 'name': city.name} for city in state.cities]
        })

    for amenity in amenities.values():
        amenities_list.append({
            'name': amenity.name
        })

    return render_template('10-hbnb_filters.html', states=states_by_cities, amenities=amenities_list)

@app.teardown_appcontext
def teardown(exception):
    '''remove the current sqlalchemy session'''
    if exception:
        print(f"{exception}")
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
