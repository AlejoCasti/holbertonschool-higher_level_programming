#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    for index, i in enumerate(my_list):
        if index == idx:
            return i
    return None
