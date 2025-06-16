#!/usr/bin/python3
'''a view for user objects'''

from models import storage
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.user import User
from models.place import Place
from models.city import City


@app_views.route('/users', strict_slashes=False)
def retrieve_users():
    '''retrieve users'''
    users = storage.all(User)
    if users is None:
        abort(404)

    users_list = []
    for user in users.values():
        users_list.append(user.to_dict())

    return users_list


@app_views.route('/users/<user_id>', strict_slashes=False)
def retrieve_user(user_id):
    '''retrieves a user'''
    user = storage.get(User, user_id)
    if user is None:
        abort(404)

    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    '''deletes a user'''
    user = storage.get(User, user_id)
    if user is None:
        abort(404)

    storage.delete(user)
    storage.save()

    return jsonify({}), 200


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    '''creates a user'''
    request_data = request.get_json()
    if request_data is None:
        abort(400, description='Not a JSON')

    email = request_data.get('email')
    if email is None:
        abort(400, description='Missing email')

    password = request_data.get('password')
    if password is None:
        abort(400, description='Missing password')

    user = User(**request_data)
    user.save()

    return jsonify(user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    '''updates a user'''
    request_data = request.get_json()
    if request_data is None:
        abort(400, description='Not a JSON')

    user = storage.get(User, user_id)
    if user is None:
        abort(404)

    if 'password' in request_data:
        password = request_data.get('password')
        user.password = password

    if 'last_name' in request_data:
        last_name = request_data.get('last_name')
        user.last_name = last_name

    if 'first_name' in request_data:
        first_name = request_data.get('first_name')
        user.first_name = first_name

    user.save()

    return jsonify(user.to_dict()), 200
