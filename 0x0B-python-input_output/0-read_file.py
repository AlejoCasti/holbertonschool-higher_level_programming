#!/usr/bin/python3
""" Read a file named as filename """


def read_file(filename=""):
    """ read file function """
    with open(filename, 'r') as fil:
        print(fil.read(), end='')
