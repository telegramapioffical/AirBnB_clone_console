#!/usr/bin/python3
'''Tests for BaseModel class'''

import unittest
from models.base_model import BaseModel

class TestBase_Model(unittest.TestCase):
    '''start tests'''

    def setUp(self):
        '''Object created from a class'''
        self.my_object = BaseModel()

    def test_is_an_instance(self):
        '''check if my_object is an instance of BaseModel'''
        self.assertIsInstance(self.my_object, BaseModel)

    def test_id(self):
        '''test if the id of two instances are different'''
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_str(self):
        '''check if the output of str is in the specified format'''
        _dict = self.my_object.__dict__
        string1 = "[BaseModel] ({}) {}".format(self.my_object.id, _dict)
        string2 = str(self.my_object)
        self.assertEqual(string1, string2)

    def test_save(self):
        '''check if the attribute updated_at (date) is updated for
        the same object with the current date'''
        first_updated = self.my_object.updated_at
        self.my_object.save()
        second_updated = self.my_object.updated_at
        self.assertNotEqual(first_updated, second_updated)

    def test_to_dict(self):
        '''check if to_dict returns a dictionary, if add a class
        key with class name of the object and if updated_at and
        created_at are converted to string object in ISO format.'''
        my_dict_model = self.my_object.to_dict()
        self.assertIsInstance(my_dict_model, dict)
        for key, value in my_dict_model.items():
            flag = 0
            if my_dict_model['__class__'] == 'BaseModel':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in my_dict_model.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)

    def test_kwargs(self):
        '''check when a dictionary in sent as **kwargs argument'''
        self.my_object.name = "Holberton"
        self.my_object.my_number = 89
        my_object_json = self.my_object.to_dict()
        my_object_kwargs = BaseModel(**my_object_json)
        self.assertNotEqual(my_object_kwargs, self.my_object)
