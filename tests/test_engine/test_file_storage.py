#!/usr/bin/python3
'''test file stirage'''

import os
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import json


class TestFileStorage(unittest.TestCase):
    '''Tests class file storage'''
    def setUp(self):
        '''set up test environment before each test'''
        self.file_path = 'test_file.json'
        FileStorage._FileStorage__file_path = self.file_path
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        '''clean up test environment'''
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        '''test if this method retuens all objects'''
        base = BaseModel()
        obj_dict = base.to_dict()

        storage = FileStorage()
        key = f"BaseModel.{base.id}"
        storage.new(base)
        storage.reload()

        self.assertIn(key, storage.all())

    def test_reload_empty_file(self):
        '''test reloading when a file is empty'''
        storage = FileStorage()
        storage.reload()
        self.assertEqual(storage.all(), {})

    def test_reload_base_model(self):
        '''test what happens when reloading a base model'''
        base = BaseModel()
        obj_dict = base.to_dict()
        key = f'BaseModel.{base.id}'
        data = {key: obj_dict}

        with open(self.file_path, "w") as f:
            json.dump(data, f)

        storage = FileStorage()
        storage.reload()
        reloaded_obj = storage.all().get(key)

        self.assertIsNotNone(reloaded_obj)
        self.assertIsInstance(reloaded_obj, BaseModel)
        self.assertEqual(reloaded_obj.created_at.isoformat(), obj_dict['created_at'])


if __name__ == "__main__":
    unittest.main()
