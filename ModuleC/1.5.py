# Have you heard people say, “You resemble your mother” or “You talk exactly like your father?”  
# It is very natural for children to acquire or inherit qualities from their parents.
# In a similar way, you can create classes that inherit the properties of an existing class.
# Let's explore

''' Task 1:  Inheritance '''
# Uncomment the statements, click Run and observe the output

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
print("** Object of Person Class Created **")
p = Person("Mira", "Dave")
p.printname()
print("\n** Example of Inheritance **")
class Teacher(Person):
  def displaygrade(self):
   g=input("Enter the grade you teach: ")
   print("The grade taught is: ",g)
 
t=Teacher("Piya","Doe")
t.printname()
t.displaygrade()

# What do you think happened? 
# A class Person has been created
# An object of the class person was created and the printname method was called
# A class Teacher has been created that has, inherited the attributes and methods from the Person class 
# Note: The pass keyword is used when you do not want to add any other properties or methods to the class.
# The class Person is called the Base class or Parent class.
# The class Teacher is called the Derived class or Child class.
 
''' Task 2:  Add a method to the child class '''
# Remove the keyword pass in the teacher class and write a method to
# Take the grade taught by the teacher as the input
# Display the grade taught by the teacher

# Solution done in Task 1

''' Task 3:  Override or Not '''
# You have created a child class that inherited the properties and methods from a parent.
# Did you notice that the child class did not have the __init__ function?
# Let us add the __init__() function to the child class .
# Remove the displaygrade() function, uncomment and add the below code, to the class teacher
# def __init__(self, name):
#   self.name = name
# def printname(self):
#   print(self.name)

# What do you think will happen? 
# Let's take a look. Uncomment the statements and click Run.
# What did you notice?   
# You will get a TypeError
# When you add the __init__() function in the child class, it no longer inherits the parent's class  __init__() function.
# To keep the inheritance of the parent's __init__() function, you can either:
# - Call to the parent's __init__() function
# - Use the super() Function.
# Change the child class __init__ function to the code given below:

#class Teacher(Person):
# def __init__(self, fname,lname):
#   Person.__init__(self, fname, lname)
#  def printname(self):
#   print(self.firstname,self.lastname)

# Now Run and see if you still get the error.

# Solution:

class Person:
 def __init__(self, fname, lname):
   self.firstname = fname
   self.lastname = lname
 
 def printname(self):
   print(self.firstname, self.lastname)
 
class Teacher(Person):
  def __init__(self, fname,lname):
    Person.__init__(self, fname, lname)
  def printname(self):
    print(self.firstname,self.lastname)


''' Task 4: Polygons '''
# Do you know what a polygon is?
# We have created a class called Polygon where the __init__ function initializes :
# - the number of sides of the polygon
# - a list that will hold the length of each side
# Uncomment the code to create the Polygon class.

#class polygon: 
#  def __init__(self, sides):
#    self.no_of_sides = sides
#    self.side=[0 for i in range(sides)]

# Now within the Polygon class you need to 
# Create a function plength() to get the user to input the length of each side and stor it to the list
# Create a method display() that displays the length of each side
# Create a class rectangle that inherits the properties of the polygon class
# Create a function within the rectangle class to calculate the area of the rectangle.

class polygon: 
 def __init__(self, sides):
   self.no_of_sides = sides
   self.side=[0 for i in range(sides)]
 def plength(self):
    for i in range(int(self.no_of_sides)):
     self.side[i]=int(input("Enter the side length: "))     
 
 def display(self):
   for i in range(len(self.side)):
     print("Length of the side: ",self.side[i])   
 
# Inherited from Polygon class
class rectangle(polygon):
 def area(self):
   rearea=self.side[0]*self.side[1]
   print("Area is of rectangle is: ",rearea)
 
t=rectangle(2)
t.plength()
t.display()
t.area()


''' Awesome!!  You did a great job applying the concept of inheritance. '''


