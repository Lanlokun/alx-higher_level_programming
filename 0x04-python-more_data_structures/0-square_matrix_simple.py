#!/usr/bin/python3

"""
return a new matrix with all values squared

"""
def square_matrix_simple(matrix=[]):
     tmp = []
     for x in matrix:
        tmp.append(list(map(lambda x: x**2, x)))
     return (tmp)
            
            
