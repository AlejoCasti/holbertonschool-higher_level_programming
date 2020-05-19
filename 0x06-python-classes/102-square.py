#!/usr/bin/python3

""" Class square """


class Square:
    """ function that initialize values """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def __lt__(self, other):
        """ less than """
        return self.area() < other.area()

    def __le__(self, other):
        """ less equals """
        return self.area() <= other.area()

    def __eq__(self, other):
        """ equals """
        return self.area() == other.area()

    def __ne__(self, other):
        """ not equals """
        return self.area() != other.area()

    def __gt__(self, other):
        """ grather than """
        return self.area() > other.area()

    def __ge__(self, other):
        """ grather equals """
        return self.area() >= other.area()

    """ get area of square """
    def area(self):
        return self.__size ** 2
    """ Getter"""
    @property
    def size(self):
        return self.__size
    """ Setter"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
