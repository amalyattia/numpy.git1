# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16s4GQCDZFDL66OkUk69ItXSp2ukZc-0U
"""

from array import array #ex1
arra1 = array('b', [1,2,3,4])
print(arra1.tolist())

#ex2
import numpy as np
u=np.array([[1,2,3],[4,5,6],[7,8,9]])
S=0
x=u.shape
row=x[0]
for i in range (row):
  S=S+u[i,i]
print(S)

import numpy as np #ex3
a = np.array([[1,2], [3,5]])
print("Original array: ")
print(a)
print("Values bigger than 3 =", a[a>3])

import numpy as np #ex4
A=np.array([1, 2, 3, 4])
B=np.array([5,6,7,8])
C=A+B
print(C)

D=np.subtract(A, B) #ex5
print(D)