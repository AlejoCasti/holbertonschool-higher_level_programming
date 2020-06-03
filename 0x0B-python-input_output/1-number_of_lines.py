#!/usr/bin/python3
""" Read a file named as filename """


def number_of_lines(filename=""):
    with open(filename, 'r') as fil:
        idx = 0
        for i in fil:
            idx += 1
        return idx
