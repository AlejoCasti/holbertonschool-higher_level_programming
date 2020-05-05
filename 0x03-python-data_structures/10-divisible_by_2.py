#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list[:]
    for index, i in enumerate(my_list):
        if i % 2 == 0:
            new_list[index] = True
        else:
            new_list[index] = False
    return new_list
