#!/usr/bin/python3
""" class Node """


class Node:
    """ constructor function """
    def __init__(self, data, next_node=None):
        """ """
        if type(data) is not int:
            raise TypeError('data must be an integer')
        if type(next_node) is not Node and next_node is not None:
            raise TypeError('next_node must be a Node object')
        self.__data = data
        self.__next_node = next_node

    """ getter data"""
    @property
    def data(self):
        return self.__data
    """ setter data"""
    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    """ getter next_node"""
    @property
    def next_node(self):
        return self.__next_node
    """ setter next_node """
    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """ constructor function"""
    def __init__(self):
        """ """
        self.__head = None

    def __str__(self):
        """ """
        if self.__head is None:
            return ""
        lista = str(self.__head.data)
        tmp_node = self.__head.next_node
        while tmp_node is not None:
            lista += "\n" + str(tmp_node.data)
            tmp_node = tmp_node.next_node
        return lista

    def sorted_insert(self, value):
        new_node = Node(value)
        tmp_node = self.__head
        counter = 0
        if self.__head is None:
            self.__head = new_node
            return
        else:
            while tmp_node.next_node is not None:
                if counter == 0 and tmp_node.data >= value:
                    new_node.next_node = self.__head
                    self.__head = new_node
                    return
                if (tmp_node.data <= value) and\
                   (tmp_node.next_node is None
                        or tmp_node.next_node.data > value):
                    new_node.next_node = tmp_node.next_node
                    tmp_node.next_node = new_node
                    return
                tmp_node = tmp_node.next_node
                counter += 1
            new_node.next_node = tmp_node.next_node
            tmp_node.next_node = new_node
