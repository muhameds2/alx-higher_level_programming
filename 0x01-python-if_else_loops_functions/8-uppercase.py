#!/usr/bin/python3
def uppercase(str):
    temp = ""
    for i in str:
        numval = ord(i)
        if numval >= 65 and numval <= 90:
            temp = temp + chr(numval)
        elif numval >= 97 and numval <= 122:
            numval = numval - 32
            temp = temp + chr(numval)
        else:
            temp = temp + chr(numval)
    print("{}".format(temp))
