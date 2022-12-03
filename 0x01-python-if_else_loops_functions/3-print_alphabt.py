#!/usr/bin/python3

# Prints all ascii letters except q and e

i = 0
while i < 26:
    if i+97 != 101 and i+97 != 113:
        print("{}".format(chr(i + 97)), end="")
    i += 1


