#!/usr/bin/python3

def print_matrix_integer(matrix=[]):
    for i in range(0, len(matrix)):
        for y in range(0, len(matrix[i])):
            if y != len(matrix[i]):
                print("{:d}".format(matrix[i][y]), end=' ')
            else:
                print("{:d}".format(matrix[i][y]), end='')
        print('')
