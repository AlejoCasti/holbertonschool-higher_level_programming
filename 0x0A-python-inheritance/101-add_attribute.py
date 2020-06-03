#!/usr/bin/python3
"""Documentation """


def add_attribute(obj, name, value):
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
