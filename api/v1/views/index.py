#!/usr/bin/python3
'''index file'''


from models import storage
from api.v1.views import app_views
from flask import jsonify
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.user import User
from models.place import Place
from models.city import City


@app_views.route('/status', strict_slashes=False)
def status():
    '''return json status'''
    return jsonify({'status': "OK"})

@app_views.route('/stats', strict_slashes=False)
def retrieve_stats():
    '''retrieves the number of each objects by type'''
    stats = {}
    classnames = {
            'amenities': Amenity,
            'states': State,
            'cities': City,
            'places': Place,
            'reviews': Review,
            'users': User
            }

    for key, cls in classnames.items():
        '''iterate through each class'''
        stats[key] = storage.count(cls)

    return jsonify(stats)
