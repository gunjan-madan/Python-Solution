# Can we automatically calculate the  age of a person or find out if the current year is a leap year or not.
# Let's take a look.  

'''Task 1: All about dates'''
print("***** Task 1: *****")
print()
# Well!!Python has a module called datetime to work with dates and perform calculations.
# Uncomment the statements below and click Run

import datetime
x = datetime.datetime.now()
print("The current date is: ", datetime.datetime.now())
print("The date today is: ",x.day)
print("The current month is: ", x.month)
print("The current year is: ", x.year)

# What do you think the program does? 
# Here is a list of some of the datetime functions that have been used in the above program:
# datetime.now()- Displays the current date 
# day - Displays the current date from the date returned by the datetime.now() function
# month - Displays the current month from the date returned by the datetime.now()
# year - Displays the current year from the date returned by the datetime.now()
# Write a program that calculates the age of a person using the list of functions given in the table. 
import datetime
x = datetime.datetime.now()
print("The date today is: ",x)
mth=int(input("Enter your birth month (in number):"))
yr=int(input("Enter your birth year (in number):"))
if x.month > mth:
  p=x.month-mth
  y=x.year-yr
  print("You are ", y,"years and ",p," months old")
else:
  p=12-(mth-x.month)
  y=x.year-(yr+1)
  print("You are ", y,"years and ",p," months old")


'''Task 2: Is it a leap year or not'''
print("***** Task 2: *****")
print()
# Write a program to find if the current year is a leap year or not
# Hint: Any year that is divisible by 4  or 400 is a leap year
import datetime
y=datetime.datetime.now()
if int(y.year) % 400 == 0:
 print("Leap year")
elif int(y.year) % 100 == 0:
 print("Not a leap year")
elif int(y.year) % 4 == 0:
 print(y.year ," is a Leap year") 
else:
 print(y.year," is not a leap year") 



'''Task 3: Is it a leap year or not'''
print("***** Task 3: *****")
print()
# Write a program to display the number of days in the current month
# Hint: Use the datetime.datetime.now() function to get the month 
import datetime
base = datetime.datetime.now()
print("The current date is: ",base)
if base.month in (1,3,5,7,8,10,12):
 print("There are 31 day in the current month")
elif base.month in (4,6,9,11):
 print("There are 30 days in the current month")
else:
 print("There are 28 days in the current month") 

'''Fantastic!! You are good at writing programs using the datetime module. Way to go!!'''

