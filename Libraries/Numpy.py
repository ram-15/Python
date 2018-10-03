#NumPy, which stands for Numerical Python, is a library consisting of multidimensional array objects and a collection of routines for #processing those arrays. Using NumPy, mathematical and logical operations on arrays can be performed. This tutorial explains the basics of #NumPy such as its architecture and environment. It also discusses the various array functions, types of indexing, etc. An introduction to #Matplotlib is also provided. All this is explained with the help of examples for better understanding.

"""
Comment exapmle! not actually a comment

NumPy is often used along with packages like SciPy (Scientific Python) and Mat−plotlib (plotting library). This combination is widely used as a replacement for MatLab, a popular platform for technical computing. However, Python alternative to MatLab is now seen as a more modern and complete programming language.
The ndarray object consists of contiguous one-dimensional segment of computer memory, combined with an indexing scheme that maps each item to a location in the memory block.

"""

import numpy as np

c = np.array([1,2,3])
print(type(c))

d = np.array([[1,2,3],[4,5,6]])
print((d[1]))

a = np.array([[1, 2, 3,4,5], [5,6,7,8,9], [10,11,11,11,11]],  ndmin = 10) 
print(a.ndim) #dimension

a = np.array([1, 2, 3], dtype = int) 
print (a)

# using array-scalar type 
import numpy as np 
dt = np.dtype(np.int32) 
print (dt)

# file name can be used to access content of age column 
dt = np.dtype([('age',np.int8)]) 
a = np.array([10,20,30], dtype = dt) 
print (a['age'])
print(type(a))

# dtype of array is int8 (1 byte) 
import numpy as np 
x = np.array([1,2,3,4,5,6,], dtype = np.int8) 
print (x.itemsize)

#This array attribute returns the number of array dimensions.
# an array of evenly spaced numbers 
import numpy as np 
c1 = np.array([[1,2,3] , [2,3,6]])
print (c1.ndim)

#numpy.itemsize
#This array attribute returns the length of each element of array in bytes.

# dtype of array is int8 (1 byte) 
import numpy as np 
x = np.array([1,2,3,4,5], dtype = np.int32) 
print ('item size',x.itemsize)

#The following example shows the current values of flags.
import numpy as np 
x = np.array([1,2,3,4,5]) 
print (x.flags)
#C_CONTIGUOUS (C) The data is in a single, C-style contiguous segment
#F_CONTIGUOUS (F) The data is in a single, Fortran-style contiguous segment
#OWNDATA (O) The array owns the memory it uses or borrows it from another object
#WRITEABLE (W) The data area can be written to. Setting this to False locks the data, making it read-only
#ALIGNED (A) The data and all elements are aligned appropriately for the hardware
#UPDATEIFCOPY (U) This array is a copy of some other array. When this array is deallocated, the base array will be updated with the contents of this array

print("#######" * 10)

x = np.empty([3,2],dtype='int') 
print (x)

# default if dtype is not provided, int is provided
x = np.zeros([5],dtype='float')
print(x)


x = np.zeros((2,2,2), dtype = [('x', 'int'), ('y', 'float'), ('z', 'complex')])  
print (x)

x = np.zeros((2,2), dtype = 'Bool')
print(x)


# To convert from one type to another
y = x.astype('float')
print(y)

#If you were using a non-numpy array, you could use a list comprehension:
from array import array

arr = [1, 1, 2, 3, 4]
y = [float(val) for val in arr]
print(y)


#Convert List to n-dim array

x = [[1,2,3],[1,2,3]] 
a = np.asarray(x) 
print (a)
print(a.ndim)

# dtype is set 
import numpy as np 

x = [1,2,3]
a = np.asarray(x, dtype = float) 
print (a)

#Convert tuple to np array
x = (1,2,3) 
a = np.asarray(x) 
print (a)

# ndarray from list of tuples 
import numpy as np 

x = [(1,2,3),(4,5)] 
a = np.asarray(x) 
print (a)

#numpy.arange
#This function returns an ndarray object containing evenly spaced values within a given range. 

# numpy.arange(start, stop, step, dtype)

x = np.arange(5,25,2,int) 
print (x)

#numpy.linspace
#This function is similar to arange() function. In this function, instead of step size, the number of evenly spaced values between the #interval is specified


#numpy.linspace(start, stop, num, endpoint, retstep, dtype)
#numpy.linspace(start, stop, num = 50, endpoint = True, retstep = False, dtype = None) : Returns number spaces evenly w.r.t interval. #Similiar to arange but instead of step it uses sample number.

#numpy.linspace(start, stop, num, endpoint, retstep, dtype)

x = np.linspace(10,25,3,True,True,int) 
print ('ss',x)

# find retstep value 
import numpy as np 

x = np.linspace(1,2,5, retstep = True) 
print (x) 
# retstep here is 0.25

#numpy.logspace
# This function returns an ndarray object that contains the numbers that are evenly spaced on a log scale. Start and stop endpoints of the # scale are indices of the base, usually 10.

# numpy.logspace(start, stop, num, endpoint, base, dtype)

# default base is 10 
a = np.logspace(1,10, 10, True, True, int) 
print (a)
