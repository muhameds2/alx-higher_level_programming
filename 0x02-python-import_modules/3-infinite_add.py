#!/usr/bin/python3
import sys
if __name__ == "__main__":
    number_of_arguments = len(sys.argv) - 1
    sum1 = 0
    for i in range(1, number_of_arguments + 1):
        sum1 += int(sys.argv[i])
    print(sum1)
