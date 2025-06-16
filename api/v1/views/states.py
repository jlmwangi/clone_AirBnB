#!/usr/bin/python3
'''a new view for state objects handling default resful api actions'''


from models import storage
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.user import User
from models.place import Place
from models.city import City


@app_views.route('/states', strict_slashes=False)
def retrieve_states():
    ''' retrieves list of all states'''
    states_list = []

    states = storage.all(State)

    for key, state in states.items():
        states_list.append(state.to_dict())

    return states_list


@app_views.route('/states/<state_id>', strict_slashes=False)
def retrieve_state(state_id):
    '''retrieve state by id'''
    states = storage.all(State)

    for key, state in states.items():
        if state.id == state_id:
            return jsonify(state.to_dict())

    abort(404)


@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    '''deletes a state by id'''
    states = storage.all(State)

    for key, state in states.items():
        if state.id == state_id:
            storage.delete(state)
            storage.save()
            return jsonify({}), 200

    abort(404)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    '''creates a state'''
    request_data = request.get_json()
    print(request_data)

    if request_data is None:
        abort(400, description='Not a JSON')

    name = request_data.get('name')
    if not name:
        abort(400, description='Missing name')

    new_state = State(name=name)
    print(new_state)

    new_state.save()

    return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    '''updates a state'''
    request_data = request.get_json()
    if request_data is None:
        abort(400, description='Not a JSON')

    name = request_data.get('name')
    if not name:
        abort(400)

    state = storage.get(State, state_id)
    if state is None:
        abort(404)

    state.name = name

    storage.save()

    return jsonify(state.to_dict()), 200
