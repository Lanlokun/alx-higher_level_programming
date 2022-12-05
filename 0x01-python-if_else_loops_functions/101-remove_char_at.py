#!/usr/bin/env python3

"""copy the content of a string removing a character at n position
"""

def remove_char_at(str, n):
    if n >= 0:
        str = str[:n] + str[n + 1:]
    return str
            