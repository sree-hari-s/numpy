# -*- coding: utf-8 -*-
"""Numpy Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aGzIW2d0c06sy1G7MSFbrSdC9G35or89
"""

#Q1
import numpy as np
arr=np.random.randint(2,11,(3,3))
arr

#Q2
import numpy as np
a=int(input("Size of array:"))
ar = np.empty(a)
for i in range(len(ar)):
  x=int(input("Element:"))
  ar[i]=x
print(ar.astype(float))

#Q3
a=np.array([10, 20, 30])
b=np.array([40,50,60,70,80,90])
np.concatenate((a,b))

#Q4
x=np.array([20,40,60])
y=np.array([100,200,300])
sumArray=np.sum((x,y))
sumArray

#Q5
array1=np.arange(10,91,10).reshape(3,3)
array1

array1[0,0:]

array1[2,2]

