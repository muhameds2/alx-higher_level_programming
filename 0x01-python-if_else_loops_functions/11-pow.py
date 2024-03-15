#!/usr/bin/python3
def pow(a, b):
    if b > 0:
        temp = 1
        for i in range(b):
            temp = temp * a
        return temp
    elif b < 0:
        temp = 1
        for i in range(-b):
            temp = temp * a
        return 1 / temp
    else:
        return 1
