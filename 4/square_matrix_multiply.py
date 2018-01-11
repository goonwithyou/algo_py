# -*- coding: utf-8 -*-
# @Time    : 2017/12/31 11:20
# @Author  : cap
# @FileName: square_matrix_multiply.py
# @Software: PyCharm Community Edition
# 俩矩阵的乘积
from numpy import matrix
from numpy import zeros
def square_matrix_multiply(A,B):
    n = len(A)
    #C = [[0 for i in range(n)]for i in range(n)]
    #C = matrix(C)
    C = zeros(shape=(n, n))
    for i in range(n):
        for j in range(n):
            C[i,j] = 0
            for k in range(n):
                C[i,j] = C[i,j] + A[i,k]*B[k,j]
    return C

# A = matrix('1 2 3; 4 5 6; 7 8 9')
# B = matrix('1 2 3; 4 5 6; 7 8 9')
# print(square_matrix_multiply(A,B))
a=[]
a.append()