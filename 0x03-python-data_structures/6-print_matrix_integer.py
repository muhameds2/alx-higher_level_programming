#!/usr/bin/python3

def print_matrix_integer(matrix=[]):
    for i in range(0, len(matrix)):
        for y in range(0, len(matrix[i])):
            print(matrix[i][y], end=' ')
        print('')
