#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = []
    values = a_dictionary.items()
    [keys.append(i[0]) for i in values if i[1] == value]
    for i in keys:
        del a_dictionary[i]
    return a_dictionary
