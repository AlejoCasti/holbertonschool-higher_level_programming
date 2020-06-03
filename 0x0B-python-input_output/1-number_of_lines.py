#!/usr/bin/python3
""" Get number of lines """


def number_of_lines(filename=""):
    """ number of lines function """
    with open(filename, 'r') as fil:
        idx = 0
        for i in fil:
            idx += 1
        return idx
