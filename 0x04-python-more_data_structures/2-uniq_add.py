#!/usr/bin/python3

def uniq_add(my_list=[]):
    if my_list is not None:
        nwset = set(my_list)
        sum = 0
        for i in nwset:
            sum += i
        return sum
    else:
        return None
