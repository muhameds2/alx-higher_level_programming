#!/usr/bin/python3
import sys

if __name__ == "__main__":
    number_of_arguments = len(sys.argv) - 1
    if number_of_arguments == 1:
        print("{} argument:".format(number_of_arguments))
        print("1: {}".format(sys.argv[1]))
    elif number_of_arguments == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(number_of_arguments))
        for i in range(1, number_of_arguments + 1):
            print("{}: {}".format(i, sys.argv[i]))
