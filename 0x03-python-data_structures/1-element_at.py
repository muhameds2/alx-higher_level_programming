#!/usr/bin/python3

def element_at(my_list, idx):
    listlen = len(my_list)
    if idx < 0 or idx > listlen - 1:
        return None
    else:
        return my_list[idx]
