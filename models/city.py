#!/usr/bin/python3
'''class city that inherits from basemodel'''

from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    ''' City class '''
    state_id = ''
    name = ''
