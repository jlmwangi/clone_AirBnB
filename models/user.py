#!/usr/bin/python3
'''a class user that inherits from base model'''

from models.base_model import BaseModel

class User(BaseModel):
    '''a user class'''
    email = ''
    password = ''
    first_name = ''
    last_name = ''

#    def __init__(self):
 #       '''initialize user class'''
  #      super().__init__()
