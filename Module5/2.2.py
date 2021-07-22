  # In one of your previous lessons, you have written a program called  "Guess the number" game by pre assigning the number to be guessed.
# Now imagine if you could get the computer to generate a random number, and then you could use that for the guessing game.
# Python provides a built-in module that you can use to generate random numbers.
# Let's take a look. 

'''Task 1: It's all Random'''
print("***** Task 1: *****")
print()
# Uncomment the statements below and click Run
import random
num=int(input("Guess a number between 0 and 10: "))
if num==random.randrange(0, 11):
 print("You guessed the right number")
else:
 print("Sorry! Better luck next time") 

# We have imported the module random and have used the function random.randrange(0, 11) to generate a number between 0 and 11. 
# Here the function randrange() returns a number between 0 (included) and 11 (not included)

'''Task 2:  Password Generator'''
print("***** Task 2: *****")
print()
# The random module can also return a random element from a given string.
# Uncomment the statements below, click Run and observe the output

#y="python"
#val=random.choice(y)
#print(val)

# Run the program 3 to 4 times and see the output changing.
# choice() shuffles the character in the string and returns random character each time.
# The choice()  function can be used in applications that require a random password to be generated.
# Ready to write a program that generates a random password. Part of the program is written for you..
# Uncomment the statements, complete the program and click Run, to execute the program

import random
passw=""
x="welcome"
y="CODING"
z="123456"
for i in range(3):
 p=random.choice(x)
 l=random.choice(y)
 t=random.choice(z)
 passw=passw+p+l+t 
print("The password generated is :",passw)


'''Task 3: Football pitch'''
print("***** Task 3: *****")
print()
# Your friend wants to create a football pitch.
# Write a program that generates a random number between 10m and 15m. This number will be used as the radius to find the area and circumference. 
# The area and circumference value will be used to create a football pitch.
# Hint: Area of circle = 3.14*radius*radius
#       Perimeter of a circle= 2*3.14*radius
import random
num=random.randrange(10, 16)
print("The radius of the football pitch is: ",num)
area=3.14*num*num
peri=2*3.14*num
print("The area of the football pitch is ",area)
print("The perim  eter of the football pitch is ",peri)



'''Fantastic!! You are getting better with working with the “random” package/module . Way to go!!'''