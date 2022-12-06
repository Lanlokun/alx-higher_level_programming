#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add

    """
    importing add_0 module

    args: a and b

    return: a + b

    """

    a = 1
    b = 2

    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))

