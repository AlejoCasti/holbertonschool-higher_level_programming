#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_v = my_list.sort()
    return max_v[-1]
