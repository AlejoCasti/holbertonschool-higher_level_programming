#!/usr/bin/python3
''' project testing '''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Square class '''
    def __init__(self, size, x=0, y=0, id=None):
        ''' constructor '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        ''' string '''
        return '[Square] ({}) {}/{} - {}'\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        ''' size - get'''
        return self.width

    @size.setter
    def size(self, value):
        ''' size - set'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        ''' update '''
        if args and len(args) > 0:
            array = ['id', 'size', 'x', 'y']
            for idx, i in enumerate(args):
                if idx == 1:
                    setattr(self, 'width', i)
                    setattr(self, 'height', i)
                else:
                    setattr(self, array[idx], i)
        else:
            for i, value in kwargs.items():
                if i == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, i, value)

    def to_dictionary(self):
        ''' to dictionary'''
        array = ['id', 'size', 'x', 'y']
        dic = dict()
        for i in array:
            if i == 'size':
                dic[i] = getattr(self, 'width')
            else:
                dic[i] = getattr(self, i)
        return dic
