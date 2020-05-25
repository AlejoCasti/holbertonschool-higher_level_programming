#!/usr/bin/python3
""" project classes """


class Rectangle:
    """ class Rectangle """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    """ Getter """
    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    """ Setter """

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    """ tostring and representation """
    def __str__(self):
        n_s = ''
        if self.height == 0 or self.width == 0:
            return n_s
        for i in range(self.height):
            n_s += ('#' * self.width) + '\n'
        return n_s

    """ public instance method """
    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width is 0 or self.height is 0:
            return 0
        return (self.width * 2) + (self.height * 2)
