#!/usr/bin/python3
def no_c(my_string):
    new_str = my_string[:]
    num = 0
    for index, i in enumerate(new_str):
        if i == 'C' or i == 'c':
            new_str = new_str[:(index - num)] + new_str[(index - num) + 1:]
            num += 1
    return new_str
