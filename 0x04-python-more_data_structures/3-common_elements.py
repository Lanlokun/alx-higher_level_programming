#!/usr/bin/python3

"""
common elements in two sets

"""

def common_elements(set_1, set_2):
    for i in set_1:
        if i in set_2:
            return i