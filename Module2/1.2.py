#Lets Learn using multiple conditions


"""-----Task 1:  What is your score? ---------"""
print(" ")
print("*** Task 1: ***")
# Write a program to get the marks for Mathematics from the user. 
# If the marks is less than 50 or equal to 50, print a message saying “you need to improve”.
# If the mark is between 50 and 80, print “ Let's work little more!”
# If the mark is more than 80, print “ You are doing good. Keep it up!”
mark1=float(input("Enter your Math score: "))
if(mark1 <= 50):
   print("you need to improve")
elif mark1<=80:
  print("Lets work little more!")
else:
   print("You are doing good. Keep it up!")


"""-----Task 2:  Which sides are equal? ---------"""
print(" ")
print("*** Task 2: ***")
#In this program we will take three sides of a triangle as input from user
#Compare the sides to check if they are equal
a=input("Enter the first side of the triangle:  ")
b=input("Enter the second side of the triangle: ")
c=input("Enter the third side of the triangle: ")
if a == b == c:
 print( "All sides are equal.")
elif a == c:
 print("The first and third side are equal.")
elif a == b:
 print("The first and second side are equal")
elif b ==c:
 print("The second and third side are equal")
else:
  print("None of the sides are equal")