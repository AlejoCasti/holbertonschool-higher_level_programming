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
    """ get area of square """
    def area(self):
        return self.__size ** 2
    """ print square"""
    def my_print(self):
        for i in range(self.__size):
            print('#' * self.__size)
