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
        if self.__size == 0:
            print('')
            return
        print('\n' * self.__position[1], end='')
        for i in range(self.__size):
            print(' ' * self.__position[0], end='')
            print('#' * self.__size)
    """ Getter """
    @property
    def position(self):
        return self.__position
    """ Setter """
    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2\
           or type(value[0]) is not int or type(value[1]) is not int\
           or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

 
