#!/usr/bin/python3

# Print numbers from 0 to 99 

i = 0

while i < 100:
    
    if i != 99:
        print("{:02d}, ".format(i), end="")
    else:
        print("{:02d}".format(i), end=" \n")
    
    i += 1
