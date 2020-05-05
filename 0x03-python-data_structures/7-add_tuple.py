#!/usr/binpython3
def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list) - 1:
        return None
    else:
        return my_list[idx]


def add_tuple(tuple_a=(), tuple_b=()):
    a = 0
    b = 0
    a += tuple_a[0] if element_at(tuple_a, 0) else 0
    b += tuple_a[1] if element_at(tuple_a, 1) else 0
    a += tuple_b[0] if element_at(tuple_b, 0) else 0
    b += tuple_b[1] if element_at(tuple_b, 1) else 0
    new_tuple = (a, b)
    return new_tuple
