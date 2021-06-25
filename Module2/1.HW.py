
'''-----Task 1: Grade Detector ------'''
print("****Task 1: ****")
print()
# write a program that takes a score as the input and then returns a grade.
# The program returns the following Grades:
#  90 or higher gets an “A”
#  80 - 89 gets a “B”
#  70 - 79 gets a “C”
#  60 - 69 gets a “D”
# Anything below a 60 receives an “F”

# You need to write the appropriate if statements, to generate the correct grades.
score =int (input ("Enter your score "))
if score >= 90:
 print ("A")
elif score >=80:
 print ("B")
elif score >=70:
 print ("C")
elif score >=60:
 print ("D")
else:
 print ("F")

'''-----Task 2: FizzBuzz Game ------'''
print("****Task 2: ****")
print()
# Write a program to accept an integer from the user. 
# If the number is a multiple of 3, print "Fizz" 
# If the number is a multiple of 5, print "Buzz"
# If the number is a multiple of 3 and 5, print "FizzBuzz"
num =int( input ("Hi, enter a number "))
if num % 3 == 0 and num % 5 == 0:
 print("fizzbuzz")
elif num % 3 == 0:
 print("fizz")
elif num % 5 == 0:
 print("buzz") 
