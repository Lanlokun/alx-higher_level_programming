#!/usr/bin/python3

#Print the last digit of a number
def print_last_digit(number):
    if number < 0:
        number = ((-1) * number) % 10
    else:
        number = number % 10

    print("{:d}\n".format(number), end="")
