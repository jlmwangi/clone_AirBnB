#!/usr/bin/python3
"""Tests base_model.py"""

import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """test base model and its methods"""

    def test_init_without_kwargs(self):
        '''tests the init method without kwargs'''
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertIsInstance(obj.id, str)
        self.assertEqual(obj.created_at, obj.updated_at)

    def test_init_with_kwargs(self):
        '''tests the init method having keyword argumens'''
        data = {
                'id': '123',
                "created_at": datetime.utcnow().isoformat(),
                'updated_at': datetime.utcnow().isoformat(),
                "__class__": "BaseModel"
        }

        obj = BaseModel(**data)

        self.assertIsNotNone(obj.id)
        self.assertIsInstance(obj.created_at, datetime)

    def test_str(self):
        '''test string method'''
        obj = BaseModel()
        expected = f"[BaseModel] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), expected)

    def test_save(self):
        '''tests the save method'''
        obj = BaseModel()
        self.assertIsInstance(obj.updated_at, datetime)

    def test_to_dict(self):
        '''tests the to_dict method'''
        obj = BaseModel()
        expected_dict = obj.to_dict()

        self.assertIn('__class__', expected_dict)
        self.assertIn('updated_at', expected_dict)

        self.assertIsInstance(expected_dict['created_at'], str)




if __name__ == "__main__":
    unittest.main()
