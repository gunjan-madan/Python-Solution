# In one of your previous goals you were introduced to the concept of class design.
# Can you tell me what an object is? 
# What are the two basic characteristics of an object? 
# Let's get a deeper understanding of how classes and objects work

''' Task 1:  Encapsulation '''

# Create a class Teacher where the properties/attributes include:
# - Name of the teacher
# - Subject the teacher teaches
# - Grade the teacher teaches
# - School in which the teacher teaches
# Create a function to display the details about the teacher
# Ensure  the attributes and methods are written inside the class. For  the class to keep them together.
# This binding of the attributes and methods inside a class  is called encapsulation.
# Encapsulation restricts access to methods and variables, thus preventing data from being accessed and modified directly.
# In the class you have created can you specify the data and functions that are encapsulated? 

# Creating a class called teacher
class teacher:
# init method
  def __init__(self, name,subject,grade,school):
    self.name=name
    self.subject=subject
    self.grade=grade
    self.school=school
 # Method/Function to display teacher details
  def displaydetails(self):
    print("Name of the teacher is:",self.name)
    print("The subject teacher teaches: ",self.subject)
    print("The Grade teacher teaches: ",self.grade)
    print("The school in which the teacher teaches: ",self.school)
# Create an object of the class
t1 = teacher("Sarah","Biology","7","DPS")
# Calling the class function
t1.displaydetails()
# More objects of the class teacher
t2 = teacher("Peter","Maths","7","St. Johns")
# Calling the class function
t2.displaydetails()


''' Task 2:  Abstraction '''
# Do you think all drivers of a car know the engine design and the internal parts of the engine? \
# Not really!! The car driver needs to know how to drive the car and does not require the knowledge of the internal parts of a car.
# The car manufacturers hide these parts from the driver and display only things they need to know in a separate panel at the front of the car.
# In a similar way, when designing a class you can decide what data or variables can be accessed outside the class as public and the ones as private .
# Uncomment the code below, and observe the code

class person:
# init method
  def __init__(self):
    self.name="priya"  
    self.__salary=2000

# What is different in the code? 
# In the code:
# - name is a public variable
# - salary is a private variable 
# A public variable is available outside the class
# A private variable is not available outside the class.
# A private variable is prefixed with a double underscore
# Now uncomment the statement below to create an instance of the class and click Run

p=person()  
print(p._person__salary)

# Did you get an error? 
# You cannot access a private variable in this way.
# - Change the print statement to:
#   print(p._person__salary)
# Now click Run. Did you get any errors?  [Wait for the student to respond]
# You need to use the class name to access the private variable. The format is:
#  instancename._Classname__private variable 
# This is called name mangling. Here you use:
# - Single underscore before the name of the class
# - Double underscore before the name of the private variable


''' Task 3:  Fund(a)bstract '''
# Create a Fund class with the following attributes:
# - Fund Account Number
# - Fund Owner Name
# - Fund Balance
# - Loan
# The fund account number,name and fund balance are public variables and Loan is a private variable.
# Create two display methods:
# - display_all_details() - all variables values to be displayed
# - display_public_details() - only public variables values to be displayed

# Creating a class called fund
class fund:
# init method
  def __init__(self, fundno,name,fundbal,loan):
    self.fundno=fundno
    self.name=name
    self.fundbal=fundbal
    self.__loan=loan
 # Method to display all details
  def display_all_details(self):
    print("Fund Number:",self.fundno)
    print("Fund Owner Name: ",self.name)
    print("Fund Balance: ",self.fundbal)
    print("Loan: ",self._fund__loan)
 # Method to display all details
  def display_public_details(self):
    print("Fund Number:",self.fundno)
    print("Fund Owner Name: ",self.name)
    print("Fund Balance: ",self.fundbal)
# Create an object of the fund class
fund1 = fund(9870,"Amit",34000,1000)
# Calling the method to display all details
print("***** DISPLAY ALL DETAILS ***** ")
fund1.display_all_details()
# Calling the method to display only public variable details
print("***** DISPLAY ONLY PUBLIC VARIABLE DETAILS ***** ")
fund1.display_public_details()


''' Great!!  You did a good job applying the concept of encapsulation and abstraction. '''


