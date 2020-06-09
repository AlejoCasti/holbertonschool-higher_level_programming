#!/usr/bin/python3
''' Testing project '''
from models.base import Base


class Rectangle(Base):
    ''' Class Rectangle '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' constructor '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        ''' string '''
        return '[Rectangle] ({}) {}/{} - {}/{}'\
            .format(self.id,
                    self.x, self.y, self.width, self.height)

    @property
    def width(self):
        ''' width - get '''
        return self.__width

    @property
    def height(self):
        ''' height - get '''
        return self.__height

    @property
    def x(self):
        ''' x - get '''
        return self.__x

    @property
    def y(self):
        ''' y - get '''
        return self.__y

    @width.setter
    def width(self, value):
        ''' width - set '''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        ''' height - get '''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        ''' x - get '''
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @y.setter
    def y(self, value):
        ''' y - get '''
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        ''' area '''
        return self.width * self.height

    def display(self):
        ''' display '''
        print('\n' * self.y, end='')
        for i in range(self.height):
            print(' ' * self.x + (self.width * '#'))

    def update(self, *args, **kwargs):
        ''' update '''
        if args and len(args) > 0:
            array = ['id', 'width', 'height', 'x', 'y']
            for idx, i in enumerate(args):
                print(i)
                setattr(self, array[idx], i)
        else:
            for i, value in kwargs.items():
                setattr(self, i, value)

    def to_dictionary(self):
        ''' to dictionary '''
        array = ['id', 'width', 'height', 'x', 'y']
        dic = dict()
        for i in array:
            dic[i] = getattr(self, i)
        return dic
