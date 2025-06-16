#!/usr/bin/python3
'''a new view for place objects to handle restful api actions'''


from models import storage
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.user import User
from models.place import Place
from models.city import City


@app_views.route('/cities/<city_id>/places', strict_slashes=False)
def retrieve_places(city_id):
    '''retrieve list of all place objects'''
    city = storage.get(City, city_id)
    if city is None:
        abort(404)

    places_list = []
    for place in city.places:
        places_list.append(place.to_dict())

    return places_list


@app_views.route('/places/<place_id>', strict_slashes=False)
def retrieve_place(place_id):
    '''retrieves a place'''
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    return jsonify(place.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'], strict_slashes=False)
def delete_place(place_id):
    '''deletes a place'''
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    storage.delete(place)
    storage.save()

    return jsonify({}), 200


@app_views.route('/cities/<city_id>/places', methods=['POST'], strict_slashes=False)
def create_place(city_id):
    ''''creates a place within a city'''

    city = storage.get(City, city_id)
    if city is None:
        abort(404)

    request_data = request.get_json()
    if request_data is None:
        abort(400, description='Not a JSON')

    if 'name' not in request_data:
        abort(400, description='Missing name')

    if 'user_id' not in request_data:
        abort(400, description='Missing user_id')

    user = storage.get(User, request_data.get('user_id'))
    if user is None:
        abort(404)

    place = Place(**request_data, city_id=city_id)
    place.save()

    return jsonify(place.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_place(place_id):
    '''updates a place'''
    request_data = request.get_json()
    if request_data is None:
        abort(400, description='Not a JSON')

    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    if 'name' in request_data:
        name = request_data.get('name')
        place.name = name

    if 'description' in request_data:
        description = request_data.get('description')
        place.description = description

    if 'number_rooms' in request_data:
        number_rooms = request_data.get('number_rooms')
        place.number_rooms = number_rooms

    if 'number_bathrooms' in request_data:
        number_bathrooms = request_data.get('number_bathrooms')
        place.number_bathrooms = number_bathrooms

    if 'max_guest' in request_data:
        max_guest = request_data.get('max_guest')
        place.max_guest = max_guest

    if 'price_by_night' in request_data:
        price_by_night = request_data.get('price_by_night')
        place.price_by_night = price_by_night

    if 'latitude' in request_data:
        latitude = request_data.get('latitude')
        place.latitude = latitude

    if 'longitude' in request_data:
        longitude = request_data.get('longitude')
        place.longitude = longitude

    storage.save()

    return jsonify(place.to_dict()), 200


@app_views.route('/places_search', methods=['POST'], strict_slashes=False)
def places_search():
    '''Retrieve Place objects based on states, cities, and amenities filters'''
    try:
        request_data = request.get_json()
    except Exception:
        return jsonify({"error": "Not a JSON"}), 400

    if request_data is None or all(len(request_data.get(key, [])) == 0 for key in ('states', 'cities', 'amenities')):
        # No filters provided — return all places
        places = [place.to_dict() for place in storage.all(Place).values()]
        return jsonify(places)

    amenity_ids = request_data.get('amenities', [])
    cities_filter = set(request_data.get('cities', []))
    states_filter = set(request_data.get('states', []))

    places_set = set()

    if states_filter:
        for state_id in states_filter:
            state = storage.get(State, state_id)
            if state:
                for city in state.cities:
                    for place in city.places:
                        places_set.add(place)

    if cities_filter:
        for city_id in cities_filter:
            city = storage.get(City, city_id)
            if city:
                for place in city.places:
                    places_set.add(place)

    # If neither state nor city filter was applied, get all places
    if not places_set:
        places_set = set(storage.all(Place).values())

    final_places = []
    for place in places_set:
        if amenity_ids:
            place_amenities = [amenity.id for amenity in place.amenities]
            if not all(aid in place_amenities for aid in amenity_ids):
                continue
        final_places.append(place.to_dict())

    return jsonify(final_places)
