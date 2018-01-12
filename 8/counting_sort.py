# -*- coding: utf-8 -*-
# @Time    : 2018/1/11 11:25
# @Author  : cap
# @FileName: counting_sort.py
# @Software: PyCharm Community Edition

def counting_sort(A):
    k = max(A)
    l = len(A)
    B = [None]*l
    C = [0]*(k+1)

    for i in range(l):
        C[A[i]] = C[A[i]] + 1
    for i in range(k):
        C[i+1] = C[i+1] + C[i]
    for i in range(l-1,-1,-1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] = C[A[i]] - 1
    return B

#test
A = [2,5,3,0,2,3,0,3,8,9,10,30,21,16]
B = counting_sort(A)
print(B)