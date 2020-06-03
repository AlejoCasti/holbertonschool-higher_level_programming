#!/usr/bin/python3
""" documentation """


def pascal_triangle(n):
    """ pascal triangle """
    li = []
    for i in range(n):
        li.append([])
        for j in range(i + 1):
            if j == 0 or j == i:
                li[i].append(1)
            else:
                li[i].append(li[i - 1][j - 1] + li[i - 1][j])
    return li
