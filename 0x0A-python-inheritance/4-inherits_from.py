#!/usr/bin/python3
""" documentation """


def inherits_from(obj, a_class):
    """ Check if is instance """
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
