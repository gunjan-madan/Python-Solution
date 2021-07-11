#Built in functions
#Function to learn:
#abs()
#sum()
#divmod()
#max()
#min()
#pow()
#round()

'''Task 1: Absolute value'''
print("***** Task 1: ***** ")
print()
#Uncomment the following
# number1 = 12
# number2 =20
# print(number1-number2)
# print(abs(number1-number2))


# abs() is a built-in function that returns the absolute value of a number. 
# With a negative number, abs() will return a positive number as absolute values are always positive numbers or zero.

# Now  write a program that takes a positive or negative number as the input  and displays it as a positive number.

'''Task 2: What's the total?'''
print("***** Task 2: ***** ")
print()
# Imagine you have been given the task of calculating the sum of all the numbers in the range of 0 to10.
# Can you write a program for the same?
# Your program might have been on the similar line:

#tot=0
#for i in range(0,11):
# tot=tot+i
#print(tot) 
# Uncomment the statement and see how it works::
#tot=sum(range(0,11))
#print(tot)

# The way sum works is: sum(iterable, start)
#  - where iterable can be a list of numbers or a range of numbers.
#  - start is an optional parameter start, that will be added to the final sum. Since it is optional, if you do not specify it is taken as 0.


# Can you tweak the program to print the total of odd numbers in the range of 0 to 10?
print("Sum of odd numbers in the range of 0 to 10")
tot=sum(range(1,10,2))
print(tot)

'''Task 3: Maximum or Minimum'''
print("***** Task 3: ***** ")
print()
# Python has two inbuilt functions that will help you find the maximum and minimum quickly.
# Uncomment the statements below and click Run

#print("Check this out!!")
#x=56
#y=90
#z=78
#p=max(x,y,z)
#s=min(x,y,z)
#print(p)
#print(s)
#print("Here is another one!!")
#x="A"
#y="G"
#z="U"
#p=max(x,y,z)
#s=min(x,y,z)
#print(p)
#print(s)

# Uncomment the statement below and observe the result:

#grades = "AABABBACBAABCD"
#print(max(grades))

'''Task 4: What's your score'''
print("***** Task 4: ***** ")
print()
# Write a program that takes the following input from five students:
# - Grade/Class
# - Scores in the following subjects - Mathematics, Science and English
# Your program then needs to display the highest score for that student


for i in range(5):
 name=input("Enter your name: ")
 mths=float(input("Enter your Maths score:"))
 eng=float(input("Enter your English score: "))
 cs=float(input("Enter your Computer Science score: "))
 print("The highest", name," has scored is: ", max(mths,eng,cs))

'''Task 5: Divisible or Not'''
print("***** Task 5: ***** ")
print()
# Do you remember the operators you would use to find the remainder and quotient of a division operation? 
# Using the divmod() function you can find both through a single operation. Here is how you would do it:
# Uncomment the statements below, run them and analyze the oupt you get:

#print(divmod(8,3))
#print(divmod(11,4))
#print(divmod(10,2.5))
#print(divmod(52.2,12))

#We can also use two variables to store the value of quotient and remainder

# q,r = divmod(13,5)
# print(q,r)

'''Task 6: Prime or Not'''
print("***** Task 5: ***** ")
print()
#Write the program to take a input from user and check if it is a prime or not(using divmod)


number= int(input("Enter the number: "))
x=2
count=0
while x<number:
  q,r = divmod(number, x)
  if r==0:
    print("Not a prime number")
    break
  x+=1
  count+=1

if count== (number-2):
  print("The number is Prime number")


  '''Task 7: Power and Roundoff'''
print("***** Task 7: ***** ")
print()
#pow(x,y) : Computes x to the power of y.
# round(number, digits): Will round up the number to decimal point specified by digits.

# Uncomment the statements below and observe the result   
#print(pow(3,2))
#print(round(3.14159,2))


'''Task 8: Let's go for lunch'''
print("***** Task 8: ***** ")
print()
# StudMonkey is feeling hungry, he takes his friends for lunch
# They decided to split the bill amount of INR 187.93 into two equal parts. The tip money which is 20% of the bill amount is added to the total amount.
# Can you write a program to help calculate the total bill amount and how much each needs to pay.

bill = 187.93 # Total bill
tip = 0.2 # 20% tip
split = 2 # Number of people splitting the bill
total = bill + (bill * tip)
each_pay = total / split
print("The amount to be paid by each: ",round(each_pay,2))

'''Great! You are getting really good with working with built-in functions.'''