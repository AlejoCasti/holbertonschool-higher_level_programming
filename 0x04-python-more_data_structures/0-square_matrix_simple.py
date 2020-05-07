def square_matrix_simple(matrix=[]):
    def pow(listt):
        return [i ** 2 for i in listt]

    def mat(matr):
        return [pow(a) for a in matr]
    matrix = mat(matrix)
    return matrix
