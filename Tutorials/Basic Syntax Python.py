# Class name starts with upper case
# Starting an identifier with a single leading underscore indicates that the identifier is private.
# Starting an identifier with two leading underscores indicates a strongly private identifier.
# If the identifier also ends with two trailing underscores, the identifier is a language-defined special name.
# The triple quotes are used to span the string across multiple lines. For example, all the following are legal −

#Python Strings
str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])     # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string

print('**********' * 10)


#Python List
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)          # Prints complete list
print (list[0])       # Prints first element of the list
print (list[1:3])     # Prints elements starting from 2nd till 3rd 
print (list[2:])      # Prints elements starting from 3rd element
print (tinylist * 2)  # Prints list two times
print (list + tinylist) # Prints concatenated lists

print('**********' * 10)

#A tuple is another sequence data type that is similar to the list. A tuple consists of a number of values separated by commas. Unlike lists, however, tuples are enclosed within parentheses.
#The main differences between lists and tuples are: Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed, while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. Tuples can be thought of as read-only lists.

#!/usr/bin/python

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)           # Prints complete list
print (tuple[0])        # Prints first element of the list
print (tuple[1:3])      # Prints elements starting from 2nd till 3rd 
print (tuple[2:])       # Prints elements starting from 3rd element
print (tinytuple * 2)   # Prints list two times
print (tuple + tinytuple) # Prints concatenated lists

print('**********' * 10)
#Python Dictionary

#Python's dictionaries are kind of hash table type. They work like associative arrays or hashes found in Perl and consist of key-value pairs. A dictionary key can be almost any Python type, but are usually numbers or strings. Values, on the other hand, can be any arbitrary Python object.

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

print("**********" * 10)


##FOR LOOP
# Simple for loop
for i in range(0,5):
	print(i)

j = 15
for j in range(20,10): 
	print(j)

fruits = ['apple', 'mango', 'cherry', 'jam']
for i in range(len(fruits)) : 
	print(fruits[i])

print(len(fruits))

print('\n');


for j in range(0,10,2): # 5 specifies increment sequence 
	print(j)

print('\n');

# Else in for loop
# Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6): 
	print(x)
else:
	print("finally finished");


#Break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break

#if and elif
a = 33
b = 33
if (b > a):
  print("b is greater than a")
elif (a == b):
  print("a and b are equal")

#Short Hand If

if a > b: print("a is greater than b")

#The while Loop


i = 1
while i < 6:
  print(i)
  i += 3

  #CHECK ELEMENT IS PRESENT IN STRING 

a = [4,2,3,1,5,6]
if 7 in a:
    a.index(6)

for letter in 'Python':     # First Example
   print ("Current Letter :", letter)

b = a.reverse()
print(b)
print(a)


print('$$$$$$$$$$' * 2);

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

#!/usr/bin/python
import calendar

cal = calendar.month(2008, 1)
print ("Here is the calendar:")
print (cal)

#!/usr/bin/python

class Employee:
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)



