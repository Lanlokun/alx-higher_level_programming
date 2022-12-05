#!/usr/bin/python 

""""Prints the alphabet in reverse order, alternating lowercase and uppercase letters, not followed by a new line"""

# i = 26

# while i > 0:
#     if i % 2 == 0:
#         print("{}".format(chr(i + 96)), end="")
#     else:
#         print("{}".format(chr(i + 64)), end="")
#     i -= 1

i = 122
while i >= 97:
    flag = 0
    if i % 2 != 0:
        i = i - 32
        flag = 1
    print("{:s}".format(chr(i)), end="")
    if flag == 1:
        i = i + 32
    i = i - 1
