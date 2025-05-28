#!/usr/bin/python3
'''test case for the user model'''

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    '''unittests for user class'''
    def test_public_class_attributes(self):
        '''tests the public class attributes in user model'''
        self.assertIsInstance(User.email, str)
        self.assertIsInstance(User.password, str)
        self.assertIsInstance(User.first_name, str)
        self.assertIsInstance(User.last_name, str)



if __name__ == "__main__":
    unittest.main()
