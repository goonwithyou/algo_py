# -*- coding: utf-8 -*-
# @Time    : 2018/1/13 11:37
# @Author  : cap
# @FileName: bucket_sort.py
# @Software: PyCharm Community Edition

import math
from math import floor
def bucket_sort(A):
    n = len(A)
    B = [[]for i in range(n)]
    C = []
    for i in range(n):
        index = floor(A[i]*n)
        B[index].append(A[i])

    for i in range(n):
        B[i] = sorted(B[i])

    for i in range(n):
        if len(B[i]) != 0:
            C.extend(B[i])

    return C

# test
A = [0.78,0.17,0.39,0.26,0.72,0.94,0.21,0.12,0.23,0.68]
print(bucket_sort(A))
