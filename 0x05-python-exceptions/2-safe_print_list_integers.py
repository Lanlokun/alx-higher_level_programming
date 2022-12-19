#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    list_len = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            i += 1
            list_len += 1
        except (TypeError, ValueError):
            pass
    print()
    return list_len
    return i