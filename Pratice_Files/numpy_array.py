# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 23:50:22 2024

@author: sm689
"""

import numpy as np


ar = np.array(12) #array with single value
print(ar) 
print(type(ar))

#1D -array
ar1 = np.array([1,3,5,7,9])
print(ar1)
print(type(ar1))


#2D-array


ar2 = np.array( [ [1,3,5,7,9 ],
                 [2,4,6,8,10] ]) 
print(ar2)



#3d-array

ar3 = np.array( [ [[1,2],[3,4]], [[5,6],[7,8]]  ])
print(ar3)




#ndmin ->we can chang the dimension 
ar4 = np.array([1,2,3,4,5,6],ndmin = 3)
print(ar4)


#attributes in the numpy
ar1 = np.array([1,3,5,7,9])

ar2 = np.array([[1,2,3],[4,5,6]]) 
ar3 = np.array([[[1,1],[2,2]],[[3,3],[4,4]]])
ar4 = np.array([1,2,3,4],ndmin = 4)


print(ar1.ndim)

print(ar2.ndim)


print(ar3.ndim)


print(ar4.ndim)
 
#it will give the shape of the array/dimesnion
print(ar1.shape)
 
print(ar2.shape) 

print(ar3.shape) 

print(ar4.shape)

#it will gives the type  
print(ar1.dtype)
print(ar2.dtype)
print(ar3.dtype)


#it will divide the size of array in bytes
print(ar1.itemsize) 

print(ar2.itemsize)

#it will print the total  bytes consumed inn the memory
print(ar1.nbytes)





