#!/usr/bin/python3
'''a view for link between place and amenity objects'''


from models import storage
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.user import User
from models.place import Place
from models.city import City



