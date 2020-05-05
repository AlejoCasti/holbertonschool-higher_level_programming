#!/usr/bin/python3
def element_at(my_list, idx):
    retorn = None
    if idx < 0:
        return None
    retorn = [i for index, i in enumerate(my_list) if index == idx]
    return retorn[0]
