#!/usr/bin/python3

def max_integer(my_list=[]):
    maxvalue = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > maxvalue:
            maxvalue = my_list[i]
    return maxvalue
