#!/usr/bin/python3
''' Project testing '''
import json


class Base:
    ''' class base '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' constructor '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''  to json string '''
        if list_dictionaries is not None and len(list_dictionaries) > 0:
            return json.dumps(list_dictionaries)
        return '[]'

    @classmethod
    def save_to_file(cls, list_objs):
        '''  save to file '''
        lis = []
        if list_objs is not None and len(list_objs) > 0:
            lis = [i.to_dictionary() for i in list_objs]
        stri = Base.to_json_string(lis)
        with open(cls.__name__ + '.json', 'w') as f:
            f.write(stri)

    @staticmethod
    def from_json_string(json_string):
        ''' from json string '''
        if json_string is not None and json_string != '':
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        ''' create '''
        if cls.__name__ == 'Rectangle':
            ins = cls(2, 2)
        if cls.__name__ == 'Square':
            ins = cls(2)
        ins.update(**dictionary)
        return ins

    @classmethod
    def load_from_file(cls):
        ''' load from file '''
        try:
            with open(cls.__name__ + '.json', 'r') as f:
                li = Base.from_json_string(f.read())
            return [cls.create(**i) for i in li]
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        
