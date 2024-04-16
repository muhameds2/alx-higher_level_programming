#!/usr/bin/python3

for i in range(10):
    for x in range(10):
        if i < x and i == 8:
            print("{}{}".format(i, x))
        elif i < x:
            print("{}{}".format(i, x), end=", ")
