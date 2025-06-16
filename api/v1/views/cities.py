#!/usr/bin/python3
'''a view for City objects'''

from models import storage
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.user import User
from models.place import Place
from models.city import City


@app_views.route('/states/<state_id>/cities', strict_slashes=False)
def retrieve_cities(state_id):
    '''retrieve cities linked to a certain state'''
    state = storage.get(State, state_id)
    if state is None:
        abort(404)

    cities_list = []
    for city in state.cities:
        cities_list.append(city.to_dict())

    return cities_list


@app_views.route('/cities/<city_id>', strict_slashes=False)
def retrieve_city(city_id):
    '''retrieves a city based on its id'''
    city = storage.get(City, city_id)
    if city is None:
        abort(404)

    return jsonify(city.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    '''deletes a city based on id'''
    city = storage.get(City, city_id)
    if city is None:
        abort(404)

    storage.delete(city)
    storage.save()

    return jsonify({}), 200


@app_views.route('/states/<state_id>/cities', methods=['POST'], strict_slashes=False)
def create_city(state_id):
    '''creates a city based on state id'''
    request_data = request.get_json()
    if request_data is None:
        abort(400, description='Not a JSON')

    name = request_data.get('name')
    if name is None:
        abort(400, description='Missing name')

    state = storage.get(State, state_id)
    if not state:
        abort(404)

    city = City(name=name, state_id=state_id)
    storage.new(city)
    storage.save()
    #city.save()

    return jsonify(city.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    '''updates a city'''
    request_data = request.get_json()
    if not request_data:
        abort(400, description='Not a JSON')

    name = request_data.get('name')
    if not name:
        abort(400)

    city = storage.get(City, city_id)
    if city is None:
        abort(404)

    city.name = name
    city.save()

    return jsonify(city.to_dict()), 200
