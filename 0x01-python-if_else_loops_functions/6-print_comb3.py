#!/usr/bin/python3

for i in range(10):
    for x in range(10):
        if i < x and x != i + 1:
            print("{}{}".format(i, x), end=", ")
        elif i < x and i == 8:
            print("{}{}".format(i, x))
