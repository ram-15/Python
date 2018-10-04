#NumPy - Indexing & Slicing

import numpy as np 
a = np.arange(10) 
s = slice(2,7,2) 
print (a[s])

import numpy as np 
a = np.arange(10) 
print(a)
b = a[2:7:2] 
print (b)

# slice single item 
import numpy as np 

a = np.arange(10) 
b = a[5] 
print (b)

# slice items between indexes 
import numpy as np 
a = np.arange(10) 
print (a[2:5])


a = np.array([[1,2,3],[3,4,5],[4,5,6]]) 
print (a) 

# slice items starting from index
print ('Now we will slice the array from the index a[1:]' )
print (a[1:])
print(a[:,1])
print(a[0,:])


#NumPy - Advanced Indexing

x = np.array([[1, 2], [3, 4], [5, 6]]) 
y = x[[0,0,0], [0,0,0]] 
print (x)
print (y)

####################################################################

x = np.array([
	[ 0,  1,  2],
	[ 3,  4,  5],
	[ 6,  7,  8],
	[ 9, 10, 11]]) 
   
print ('Our array is:') 
print (x) 
print ('\n') 

rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]]) 
y = x[rows,cols] 
   
print ('The corner elements of this array are:') 
print (y)

##################################################################

import numpy as np 
x = np.array([
	[ 0,  1,  2],
	[ 3,  4,  5],
	[ 6,  7,  8],
	[ 9, 10, 11]]) 

print ('Our array is:') 
print (x)
print ('\n')  

# slicing 
z = x[1:4,1:3] 
print (z) 
print ('\n') 

# using advanced index for column 
y = x[1:4,[1,2]] 

print ('Slicing using advanced index for column:') 
print (y)

############################################################

import numpy as np 
a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]]) 
b = np.array([1.0,2.0,3.0])  
   
print ('First array:') 
print (a)
print ('\n') 
   
print ('Second array:') 
print (b) 
print ('\n')  
   
print ('First Array + Second Array') 
print (a + b)

##############################################################
#numpy.amin() and numpy.amax()

import numpy as np 
a = np.array([[3,7,5],[8,4,3],[2,4,9]]) 

print ('Our array is:') 
print (a)  
print ('\n')  

print ('Applying amin() function:') 
print (np.amin(a,1)) 
print ('\n')  

print ('Applying amin() function again:') 
print (np.amin(a,0)) 
print ('\n')  

print ('Applying amax() function:') 
print (np.amax(a)) 
print ('\n')  

print ('Applying amax() function again:') 
print (np.amax(a, axis = 0))

#####################################

import numpy as np 
a = np.array([0,30,45,60,90]) 

print ('Sine of different angles:') 
# Convert to radians by multiplying with pi/180 
print (np.sin(a*np.pi/180)) 
print ('\n' ) 

print ('Cosine values for angles in array:' )
print (np.cos(a*np.pi/180)) 
print ('\n')  

print ('Tangent values for given angles:') 
print (np.tan(a*np.pi/180)) 

print (np.arcsin(a*np.pi/180)) 
print ('\n' ) 

print ('Cosine values for angles in array:' )
print (np.arccos(a*np.pi/180)) 
print ('\n')  

print ('Tangent values for given angles:') 
print (np.arctan(a*np.pi/180)) 



#***********************************************************

import numpy as np 
x = np.array([3, 1, 2]) 

print ('Our array is:') 
print (x)
print ('\n')  

print ('Applying argsort() to x:') 
print (x)
y = np.argsort(x) 
print (x)
print ( y )
print ('\n')  

print ('Reconstruct original array in sorted order:') 
print (x[y]) 
print ('\n')  

print ('Reconstruct the original array using loop:') 
for i in y: 
   print (x[i],)


import math
print(math.cos(math.pi)) 
-1.0

print(math.pi)

nums = set([1, 1, 2, 2, 3, 3, 3, 4]) 
print(len(nums))

a=[1,2,3] 
a[1]=4
print(a)



a = [1,2,3] 

b = a 
print(a == b)
True
print(a is b) 
True 

b = a[:] 
a == b 
True
a is b 
False
print(a) 
print(b)

y = [x**2 for x in range(5)]
print(y)

print('g')
 
x = 1 
def my_function(): 
  x = 2 
  print(x) 
print(x) 
my_function() 
print(x) 

x = 1 
while x < 5: 
  x = x * 2
  print(x)



####

for integer in (-1,3,5): 
  if integer < 0: 
   print("negative") 
  else: 
   print("non-negative")



x = 'String' 
y = 10 
z = 5.0 
print(x + x) # print command 1 
print(y + y) # print command 2 
print(y + z) # print command 4 
print(y + x) # print command 3 
