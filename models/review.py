#!/usr/bin/python3
'''class Review that inherits from basemodel'''

from models.base_model import BaseModel
from models.place import Place
from models.user import User


class Review(BaseModel):
    ''' review class '''
    place_id = ''  # place.id
    user_id = ''  # user.id
    text = ''
