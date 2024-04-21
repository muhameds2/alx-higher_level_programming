#!/usr/bin/python3
import calculator_1

if __name__ == "__main__":
    a = 10
    b = 5
    summ = calculator_1.add(a, b)
    sub = calculator_1.sub(a, b)
    mul = calculator_1.mul(a, b)
    divv = calculator_1.div(a, b)
    print("{} + {} = {}".format(a, b, summ))
    print("{} - {} = {}".format(a, b, sub))
    print("{} * {} = {}".format(a, b, mul))
    print("{} / {} = {}".format(a, b, divv))
