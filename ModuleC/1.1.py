
''' Task 1:  Creating a class in Python '''
print("***** Task 1: ******")
print()
#Uncomment the statements below and observe the code:

## Creating a class called car
#class car:
 ## init method 
 #def __init__(self, mileage,model,color):
   #self.mileage=mileage
   #self.model=model
   #self.color=color
  ## Method/Function to display car details
 #def displaydetails(self):
   #print("Car model is: ",self.model)
   #print("Car mileage is: ",self.mileage)
   #print("Car color is: ",self.color)
 
## Create an object of the class
#c = car("13km/l","Hyundai i10","Black")
## Calling the class function
#c.displaydetails()


# What did you observe? 
# The code above shows you how a class with attributes and functions are created in Python. 
# The steps we followed were:
# - Step 1: Create a class using the keyword class followed by the name of the class.
# - Step 2: Create a __init__ method which is a special method to initialize the attributes or variables defined in the class.
# - Step 3: Create a function to display the data. 
# - Step 4: An object of the class car is created, where in the mileage, color and model, is passed as the parameter.
# It's time to create some more objects of the class car.
# Create objects of the class car with the following details 
# - Car Model - Ford Ikon; Mileage-14.2 km/l ; Color-Blue
# - Car Model - Toyota Corolla Altis; Mileage-16 km/l ; Color-Red
# Remember to display the details [Hint: Call the displaydetails() function]


# More objects of the class car
c1 = car("14.2km/l","Ford Ikon","Blue")
# Calling the class function
c1.displaydetails()
 
c2 = car("16 km/l","Toyota Corolla Altis","Red")
# Calling the class function
c2.displaydetails()


''' Task 2:  Get Classy '''
print("***** Task 2: ******")
print()
# Create a student class with the following attributes:
# - Name
# - Grade
# - School
# The class should have a method/function to display the details
# After defining the class, create objects to display the details of students
# Note: You can delete objects by using the del keyword
class student:
 # init method
 def __init__(self, name,grade,school):
   self.name=name
   self.grade=grade
   self.school=school
  # Method/Function to display student details
 def displaydetails(self):
   print("Student name is: ",self.name)
   print("Student grade is: ",self.grade)
   print("Student school is: ",self.school)
 
# Create an object of the class
stu1 = student("Ayush","7","DPS")
# Calling the class function
stu1.displaydetails()


''' Task 3:  More Functions '''
print("***** Task 3: ******")
print()
# Modify the program you have created in Task 2, to 
# Get the student data from the user  
# Create objects based on the user input
# Display the data
class student:
 # init method
 def __init__(self, name,grade,school):
   self.name=name
   self.grade=grade
   self.school=school
  # Method/Function to display student details
 def displaydetails(self):
   print("Student name is: ",self.name)
   print("Student grade is: ",self.grade)
   print("Student school is: ",self.school)
 
# Create an object of the class
name=input("Enter the student name: ")
grade=input("Enter the student grade: ")
school=input("Enter the school name: ")
 
stu1 = student(name,grade,school)
# Calling the class function
stu1.displaydetails()

''' Task 4:  Lets loop '''
print("***** Task 4: ******")
print()
# How would you modify the program in  task 3, to display details of 3 students?
# [Hint: Use loops]
class student:
 # init method
 def __init__(self, name,grade,school):
   self.name=name
   self.grade=grade
   self.school=school
  # Method/Function to display student details
 def displaydetails(self):
   print("Student name is: ",self.name)
   print("Student grade is: ",self.grade)
   print("Student school is: ",self.school)
# Create an object of the class
i=1
while(i<=3):
 name=input("Enter the student name: ")
 grade=input("Enter the student grade: ")
 school=input("Enter the school name: ")
 print("---------------------------")
 stu1 = student(name,grade,school)
 # Calling the class function
 print("***Details of Student ",i,"***")
 stu1.displaydetails()
 print("---------------------------")
 i=i+1

''' Task 5: Multiple Objects '''
print("***** Task 5: ******")
print()
# What happens to variables/attributes when multiple objects of a class are created?
# Will the same variables be used across the objects? 
# Lets try it out by creating multiple student objects
# Uncomment the statement, click Run and observe the output.

## Create an object of the class student
#stu1 = student("Reya","7","TBS")
#stu2 = student("Avi","8","Teamis")
## Display the details
#print("Name in stu1:",stu1.name)
#print("Grade in stu1:",stu1.grade)
#print("School in stu1:",stu1.school)
#print()
#print("Name in stu2:",stu2.name)
#print("Grade in stu2:",stu2.grade)
#print("School in stu2:",stu2.school)

# For every object a separate copy of the variables is created. 
# These variables are called instance variables.
# Modifying the instance variable for one object does not change the values in instance variables of other objects

