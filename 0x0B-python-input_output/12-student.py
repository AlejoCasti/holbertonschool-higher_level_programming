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
        if type(attrs) is not list\
           or len(set([type(j) for j in attrs])) != 1:
            return self.__dict__
        else:
            dic = {}
            for i in attrs:
                if i in self.__dict__:
                    dic[i] = self.__dict__[i]
            return dic
