#Functions
#Functions are required to reuse the code

'''Task 1:  All about functions'''
print("****** Task 1: *****")
print()
# Uncomment  the statement below and click Run.

##Define a user-defined function
#def welcome():
# print("Welcome to Cuemath Python class!!")
##Call the function
#welcome()

'''Task'''
# Write a function to print your name and grade
def details():
 print("My name is Ruth.")
 print("I study in Grade 6.")
#Call the function
details()


''' Task 2: Redefine the function '''
print("****** Task 2: *****")
print()
# Uncomment  the statements and click Run

#def studentdetails(name):
#  print("Name is:", name)
#studname=input("Enter your name: ")
#studentdetails(studname)
# Modify the program to:
# - Take the grade and age as input from the user
# - Pass the grade and age as arguments to the function

def studentdetails(name,age,grade):
 print("Name is:", name)
 print("Grade is:", grade)
 print("Age is:", age)

studname=input("Enter your name: ")
studage=input("Enter your age: ")
studgrade=input("Enter your grade: ")
print()
studentdetails(studname,studage,studgrade)


''' Task 3:  Point of return '''
print("****** Task 3: *****")
print()
# Uncomment the statement and click Run

## Define the function
#def addition(x,y):
#  z=x+y
#  return z
##Call the function
#num1=int(input("Enter the first number: ")) 
#num2=int(input("Enter the second number: "))
#print("The sum is: ",addition(num1,num2))

# The function : 
# - Takes two arguments as input
# - Adds them and returns the sum to the caller.
# A return statement helps the function pass data back to the caller.
# Modify the above function to take three arguments  and return their product
def product(x,y,z):
 p=x*y*z
 return p
 
num1=int(input("Enter the first number: ")) 
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))
print("The sum is: ",product(num1,num2,num3))

''' Task 4:  What goes around, comes around '''
print("****** Task 4: *****")
print()
# Create functions that take the radius as the argument and return the area and perimeter.
def area(r):
 area=3.14*r*r
 return area
 
def perimeter(r):
 peri=2*3.14*r
 return peri
 
num=int(input("Enter the radius: ")) 
print("Area of the circle: ",area(num))
print("Perimeter of the circle: ",perimeter(num))


''' Task 5: Convert days to second '''
print("****** Task 5: *****")
print()
# Create a function that takes the number of days as an argument , converts it to seconds and returns the same.
def convert_days_to_seconds(days):
 hours=days*24
 minutes=hours*60
 seconds=minutes*60
 return seconds
 
day=int(input("Enter the number of days: ")) 
print("The seconds is: ",convert_days_to_seconds(day))