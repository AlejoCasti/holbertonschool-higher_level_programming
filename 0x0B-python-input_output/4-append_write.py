#!/usr/bin/python3
""" append values of a file """


def append_write(filename="", text=""):
    """ append function """
    with open(filename, 'a+') as fil:
        return fil.write(text)
