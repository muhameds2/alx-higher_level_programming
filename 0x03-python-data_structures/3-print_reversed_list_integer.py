#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    rvls = list(reversed(my_list))
    for i in rvls:
        if !(isinstance(i, str)):
            print("{:d}".format(i))
