#!/usr/bin/python3
""" Read a file named as filename """


def write_file(filename="", text=""):
    with open(filename, 'w+') as fil:
        return fil.write(text)
