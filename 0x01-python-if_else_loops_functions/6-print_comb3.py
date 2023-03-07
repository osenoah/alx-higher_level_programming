#!/usr/bin/python3
for digit0 in range(0, 9):
    for digit1 in range(digit0 + 1, 10):
        if digit0 == 8:
            print("{:d}{:d}".format(digit0, digit1))
            break
        print("{:d}{:d}".format(digit0, digit1), end=", ")
