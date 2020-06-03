#!/usr/bin/python3
""" Read a file named as filename """


def append_write(filename="", text=""):
    with open(filename, 'a+') as fil:
        return fil.write(text)
