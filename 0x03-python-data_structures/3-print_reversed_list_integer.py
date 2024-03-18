#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list == []:
        return
    else:
        for i in range(-1, -(len(my_list)) - 1, -1):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]))
