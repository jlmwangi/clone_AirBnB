#!/usr/bin/python3
'''a view for the link between place objects and amenity objects'''

from models.place import Place
from models.amenity import Amenity
from models import storage
from flask import jsonify, abort, request
from api.v1.views import app_views
import os


@app_views.route('/places/<place_id>/amenities', strict_slashes=False)
def list_placeamenities(place_id):
    ''' lists all amenities of a place'''
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        place = storage.get(Place, place_id)
        if place is None:
            abort(404)

        amenities_list = []
        for amenity in place.amenities:
            amenities_list.append(amenity.to_dict())

        return amenities_list
    else:
        place = storage.get(Place, place_id)
        if place is None:
            abort(404)

        amenityids_list = place['amenity_ids']

        return amenityids_list


@app_views.route('/places/<place_id>/amenities/<amenity_id>', methods=['DELETE'], strict_slashes=False)
def delete_placeamenity(place_id, amenity_id):
    '''deletes an amenity of a certain place'''
    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        place = storage.get(Place, place_id)
        if place is None:
            abort(404)

        amenity = storage.get(Amenity, amenity_id)
        if amenity is None:
            abort(404)

        if amenity in place.amenities:
            storage.delete(amenity)
            storage.save()
        else:
            abort(404)

        return jsonify({}), 200
    else:
        place = storage.get(Place, place_id)
        if place is None:
            abort(404)

        amenity = storage.get(Amenity, amenity_id)
        if amenity is None:
            abort(404)

        if amenity_id in place['amenity_ids']:
            storage.delete(amenity)
            storage.save()
        else:
            abort(404)

        return jsonify({}), 200


@app_views.route('/places/<place_id>/amenities/<amenity_id>', methods=['POST'], strict_slashes=False)
def create_placeamenity(place_id, amenity_id):
    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        place = storage.get(Place, place_id)
        if place is None:
            abort(404)

        amenity = storage.get(Amenity, amenity_id)
        if amenity is None:
            abort(404)

        if amenity in place.amenities:
            return jsonify(amenity.to_dict()), 200
        else:
            place.amenities.append(amenity)
            storage.save()

            return jsonify(amenity.to_dict()), 201
    else:
        place = storage.get(Place, place_id)
        if place is None:
            abort(404)

        amenity = storage.get(Amenity, amenity_id)
        if amenity is None:
            abort(404)

        if amenity_id in place['amenity_ids']:
            return jsonify(amenity.to_dict()), 200
        else:
            place['amenity_ids'].append(amenity_id)
            storage.new(amenity)
            storage.save()

            return jsonify(amenity.to_dict())


