#!/usr/bin/python3
'''base class module'''

class Base:
    '''the Base class'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''init magic'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''__dict__ to json'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)
