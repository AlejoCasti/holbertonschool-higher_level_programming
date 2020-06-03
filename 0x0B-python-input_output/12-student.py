#!/usr/bin/python3
""" documentation """


class Student:
    """ class Student """
    def __init__(self, first_name, last_name, age):
        """ """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ """
        if type(attrs) is list\
           and all(isinstance(j, str) for j in attrs):
            dic = {}
            for i in attrs:
                if i in self.__dict__:
                    dic[i] = self.__dict__[i]
            return dic
        return self.__dict__
