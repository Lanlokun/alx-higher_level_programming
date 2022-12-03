#!/usr/bin/python3

# prints all possible different combinations of two digits

i = 0

while i < 100:
    if i % 10 > i / 10:
        if i != 89:
            print("{:02d}, ".format(i), end="")
        else:
            print("{:02d}".format(i), end=" ")
    i += 1