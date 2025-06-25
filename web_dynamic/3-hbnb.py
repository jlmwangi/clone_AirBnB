#!/usr/bin/python3
'''script that starts a flask application'''

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.city import City
import os
import uuid


app = Flask(__name__)

@app.route('/3-hbnb', strict_slashes=False)
def hbnb_filters():
    states_by_cities = []
    amenities_list = []
    places_list = []

    states = sorted(storage.all(State).values(), key=lambda k: k.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda k: k.name)
    places = sorted(storage.all(Place).values(), key=lambda k: k.name)

    for state in states:
        states_by_cities.append({
            'id': state.id,
            'name': state.name,
            'cities': [{'id': city.id, 'name': city.name} for city in state.cities]
        })

    for amenity in amenities:
        amenities_list.append({
            'name': amenity.name
        })

    for place in places:
        places_list.append({
            'name': place.name,
            'description': place.description,
            'number_rooms': place.number_rooms,
            'number_bathrooms': place.number_bathrooms,
            'max_guest': place.max_guest,
            'price_by_night': place.price_by_night,
#            'latitude': place.latitude,
#            'longitude': place.longitude
        })

    return render_template('3-hbnb.html', places=places_list, states=states_by_cities, amenities=amenities_list, cache_id=uuid.uuid4())

@app.teardown_appcontext
def teardown(exception):
    '''remove the current sqlalchemy session'''
    if exception:
        print(f"{exception}")
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
