#!/usr/bin/python3
""" write a file named as filename """


def write_file(filename="", text=""):
    """ write file function """
    with open(filename, 'w+') as fil:
        return fil.write(text)
