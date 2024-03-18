#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    nwlist = []
    for i in my_list:
        if i % 2 == 0:
            nwlist.append(True)
        else:
            nwlist.append(False)
    return nwlist
