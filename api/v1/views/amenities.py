#!/usr/bin/python3
'''a view for amenity objects'''

from models import storage
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.user import User
from models.place import Place
from models.city import City


@app_views.route('/amenities', strict_slashes=False)
def retrieve_amenities():
    '''retrieve amenities'''
    amenities = storage.all(Amenity)
    if amenities is None:
        abort(404)

    amenities_list = []
    for amenity in amenities.values():
        amenities_list.append(amenity.to_dict())

    return amenities_list


@app_views.route('/amenities/<amenity_id>', strict_slashes=False)
def retrieve_amenity(amenity_id):
    '''retrieves an amenity'''
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)

    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'], strict_slashes=False)
def delete_amenity(amenity_id):
    '''deletes an amenity'''
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)

    storage.delete(amenity)
    storage.save()

    return jsonify({}), 200


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_amenity():
    '''creates an amenity'''
    request_data = request.get_json()
    if request_data is None:
        abort(400, description='Not a JSON')

    name = request_data.get('name')
    if name is None:
        abort(400, description='Missing name')

    amenity = Amenity(name=name)
    amenity.save()

    return jsonify(amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'], strict_slashes=False)
def update_amenity(amenity_id):
    '''updates an amenity'''
    request_data = request.get_json()
    if request_data is None:
        abort(400, description='Not a JSON')

    name = request_data.get('name')
    if name is None:
        abort(400, description='Missing name')

    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)

    amenity.name = name
    amenity.save()

    return jsonify(amenity.to_dict()), 200
