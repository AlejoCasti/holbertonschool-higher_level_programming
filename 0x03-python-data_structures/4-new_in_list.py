#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list = my_list[:]
    if idx < 0:
        return list
    for i in range(len(list)):
        if i == idx:
            list[i] = element
    return list
