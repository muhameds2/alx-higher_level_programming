#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    number_of_arguments = len(argv) - 1
    if number_of_arguments != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] not in ("+", "-", "*", "/"):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        if argv[2] == '+':
            add = add(int(argv[1]), int(argv[3]))
            print("{} + {} = {}".format(argv[1], argv[3], add))
        elif argv[2] == '-':
            sub = sub(int(argv[1]), int(argv[3]))
            print("{} - {} = {}".format(argv[1], argv[3], sub))
        elif argv[2] == '*':
            mul = mul(int(argv[1]), int(argv[3]))
            print("{} * {} = {}".format(argv[1], argv[3], mul))
        else:
            div = div(int(argv[1]), int(argv[3]))
            print("{} / {} = {}".format(argv[1], argv[3], div))
