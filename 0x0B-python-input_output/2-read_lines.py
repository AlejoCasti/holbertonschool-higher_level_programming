#!/usr/bin/python3
""" Read a file named as filename """
number_of_lines = __import__('1-number_of_lines').number_of_lines


def read_lines(filename="", nb_lines=0):
    """ read lines function """
    with open(filename, 'r') as fil:
        if nb_lines <= 0 or nb_lines > number_of_lines(filename):
            nb_lines = number_of_lines(filename)
        for i in range(nb_lines):
            print(fil.readline(), end='')
