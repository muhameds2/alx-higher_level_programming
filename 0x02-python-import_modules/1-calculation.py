#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    a = 10
    b = 5
    summ = calculator_1.add(a, b)
    sub = calculator_1.sub(a, b)
    mul = calculator_1.mul(a, b)
    divv = calculator_1.div(a, b)
    print("{} + {} = {}".format(a, b, summ))
    print("{} - {} = {}".format(a, b, sub))
    print("{} * {} = {}\n{} / {} = {}".format(a, b, mul, a, b, divv))
