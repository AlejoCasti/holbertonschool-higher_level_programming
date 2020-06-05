#!/usr/bin/python3
""" divided whole matrix """


def matrix_divided(matrix, div):
    """ matrix divided function """
    a = len(matrix[0])
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    for i in matrix:
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    for i in matrix:
        if a != len(i):
            raise TypeError('Each row of the matrix must have the same size')
    matris = [[i for i in j if type(i) not in [int, float]] for j in matrix]
    print(matris)
    a = [[round(i/div, 2) for i in j] for j in matrix]
    return a
