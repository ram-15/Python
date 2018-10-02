class Employee: 
   
   counter = 0;
   
   def __init__(self,name):
      Employee.counter = Employee.counter + 1
      self.name = name;
   
   def greetCustomer(self):
      print('Hello ' + self.name + '')
      print(Employee.counter)

c = Employee('Sriram');
c.greetCustomer();

c = Employee('Viswanathan');
c.greetCustomer();

# ----------------------------------------------------------------------------


class Employee1: 
   
   counter = 0;
   
   def __init__(self,name):
      Employee1.counter = Employee1.counter + 1
      self.name = name;
   
   def greetCustomer(self):
      print('Hello ' + self.name + '')
      print(Employee1.counter)

c = Employee1('Sriram');
c.greetCustomer();

c = Employee1('Viswanathan');
c.greetCustomer();

#################################################################################

class Point:
   
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   
   def __del__(self):
      class_name = self.__class__.__name__
      print (class_name, "destroyed")

pt1 = Point()
pt2 = pt1
pt3 = pt1
print (id(pt1), id(pt2), id(pt3)) # prints the ids of the obejcts
del pt1
del pt2
del pt3

print('&&&&&&&&&&&&&&&&&&&&&' * 5)

class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print ("Calling parent constructor")

   def parentMethod(self):
      print ('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print ("Parent attribute :", Parent.parentAttr)

class Child(Parent): # define child class
   def __init__(self):
      print ("Calling child constructor")

   def childMethod(self):
      print ('Calling child method')

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method

#issubclass(sub, sup)
print(issubclass(Child, Parent))

# isinstance(obj, Class)
print(isinstance(c, Child))

#Overriding Methods

#!/usr/bin/python

class Parent:        # define parent class
   def myMethod(self):
      print ('Calling parent method')

class Child(Parent): # define child class
   def myMethod(self):
      print ('Calling child method')

c = Child()          # instance of child
c.myMethod()         # child calls overridden method


########################## Data Hiding ##########################
class JustCounter:
   __secretCount = 0
  
   def count(self):
      self.__secretCount += 1
      print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
#print (counter.__secretCount)

##################################################################


class a:
	counter = 10; // if --counter is accessed in sub class, error - no counter
	def __init__(self):
		print('from inside constructor');


	def method1(self, name):
		print('from inside method 1, users name', name)

class b(a):
	def __init__(self):
		print('from inside constructor');


	def method1(self, name):
		print('from inside method 2, users name', name)

	def method3(self):
		print('x',a.counter)


obj = a();
obj.method1('sriram')

obj1 = b();
obj1.method1('viswanathan')
obj1.method3()

