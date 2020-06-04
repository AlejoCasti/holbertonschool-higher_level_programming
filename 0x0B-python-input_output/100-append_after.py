#!/usr/bin/python3
""" append lines """


def append_after(filename="", search_string="", new_string=""):
    """ append_after function """
    with open(filename, mode='r') as fil:
        con = fil.read().split('\n')
        new = []
        for i in con:
            new.append(i)
            if search_string in i:
                new.append(new_string[:-1])
    with open(filename, mode='w') as f:
        f.write("\n".join(new))
