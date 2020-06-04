#!/usr/bin/python3
""" append lines """


def append_after(filename="", search_string="", new_string=""):
    """ append_after function """
    with open(filename, mode='r') as fil:
        new = []
        for i in fil:
            new.append(i)
            if search_string in i:
                new.append(new_string)
    with open(filename, mode='w') as f:
        f.write(''.join(new))
