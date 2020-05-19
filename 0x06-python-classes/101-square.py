#!/usr/bin/python3
class Square:
    # Constructor
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        if type(position) is not tuple or len(position) != 2\
           or type(position[0]) is not int or type(position[1]) is not int\
           or position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__size = size
        self.__position = position

    def __str__(self):
        string = ""
        if self.__size == 0:
            print('')
            return
        string += '\n' * self.__position[1]
        for i in range(self.__size):
            string += ' ' * self.__position[0]
            string += '#' * self.__size
            if i != self.__size - 1:
                string += '\n'
        return string

    # Getter and Setter
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2\
           or type(value[0]) is not int or type(value[1]) is not int\
           or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    # Extern function
    def area(self):
        return self.__size * 2

    def my_print(self):

        if self.__size == 0:
            print('')
            return
        print('\n' * self.__position[1], end='')
        for i in range(self.__size):
            print(' ' * self.__position[0], end='')
            print('#' * self.__size)
