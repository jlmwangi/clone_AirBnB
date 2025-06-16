#!/usr/bin/python3
'''a new view for review objects to handle restful api actions'''


from models import storage
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.user import User
from models.place import Place
from models.city import City


@app_views.route('/places/<place_id>/reviews', strict_slashes=False)
def retrieve_reviews(place_id):
    '''retrieve list of all review objects'''
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    reviews_list = []
    for review in place.reviews:
        reviews_list.append(review.to_dict())

    return reviews_list


@app_views.route('/reviews/<review_id>', strict_slashes=False)
def retrieve_review(review_id):
    '''retrieves a review'''
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)

    return jsonify(review.to_dict())


@app_views.route('/reviews/<review_id>', methods=['DELETE'], strict_slashes=False)
def delete_review(review_id):
    '''deletes a review'''
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)

    storage.delete(review)
    storage.save()

    return jsonify({}), 200


@app_views.route('/places/<place_id>/reviews', methods=['POST'], strict_slashes=False)
def create_review(place_id):
    ''''creates a review for a place'''

    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    request_data = request.get_json()
    if request_data is None:
        abort(400, description='Not a JSON')

    if 'text' not in request_data:
        abort(400, description='Missing text')

    if 'user_id' not in request_data:
        abort(400, description='Missing user_id')

    user = storage.get(User, request_data.get('user_id'))
    if user is None:
        abort(404)

    review = Review(**request_data, place_id=place_id)
    review.save()

    return jsonify(review.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def update_review(review_id):
    '''updates a review'''
    request_data = request.get_json()
    if request_data is None:
        abort(400, description='Not a JSON')

    review = storage.get(Review, review_id)
    if review is None:
        abort(404)

    text = request_data.get('text')
    if text is None:
        abort(400, description='Missing text')

    review.text = text
    storage.save()

    return jsonify(review.to_dict()), 200
