#!/usr/bin/python3
""" project classes """


class Rectangle:
    """ class Rectangle """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    """ main functions """
    def __str__(self):
        n_s = ''
        if self.height is 0 or self.width is 0:
            return n_s
        for i in range(self.height):
            n_s += (str(self.print_symbol) * self.width)
        return n_s

    def __repr__(self):
        return 'Rectangle(' + str(self.width) +\
            ', ' + str(self.height) + ')'

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    """ public instance method """
    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width is 0 or self.height is 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_2.area() == rect_1.area():
            return rect_1
        return (rect_2 if rect_2.area() > rect_1.area() else rect_1)

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
