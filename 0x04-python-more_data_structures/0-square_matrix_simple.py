#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    nw_matrix = []
    for row in range(len(matrix)):
        nw_row = []
        for column in range(len(matrix[row])):
            nw_row.append(matrix[row][column] ** 2)
        nw_matrix.append(nw_row)
    return nw_matrix
