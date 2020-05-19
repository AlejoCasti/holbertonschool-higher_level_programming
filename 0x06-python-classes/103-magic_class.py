#!/usr/bin/python3
""" math library """
import math
""" project """


class MagicClass:
    """ magic class """
    def __init__(self, radius=0):
        """ intialize """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ get area """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """ get circumference """
        return (2 * math.pi) * self.__radius
