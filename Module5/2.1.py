# Can you find or match a string or a pattern in a given string?
# Python provides a built-in package called re, which can be used with Regular Expressions. 
# A regular expression is a sequence of characters used to "find" or "find and replace" strings. It is also used for validating or checking if the user input is correct.
# Let's take a look.

'''Task 1: Pattern search'''
print("***** Task 1:******")
print()
# Uncomment the below statements and click Run. Observe the output.
#import re
#txt = "HelloWorld"
#x = re.search("World", txt)
#print(x)
#if x:
# print("Match found")
#else:
# print("Match not found")
# Let us analyze the output. 

#Let us analyze the output . 
# We have imported a module called re that can be used to work with strings- using the import command. 
# Then the program searches for the string ->"World" and returns its position

# Here is a list of search patterns you can use 
#  re.search("[a-z]",string) - Searches for any lowercase characters in the string
#  re.search("[A-Z],string) - Searches for any uppercase characters in the string
#  re.search("[$#@]",string) - Searches for special characters in the string
#  re.search("\s",string) - Searches for white-space character in the string

# Using the information given in above, complete the Python program to check the strength of a password .
# You need to check for the following:
#   -Has at least one number.
#   -Has at least one uppercase and one lowercase character.
#   -Has at least one special symbol.
#   -Should be between 6 to 20 characters long.
# Uncomment the statement and complete the program

import re                                                 
p= input("Input your password: ")
x = True
while x:                              # while loop
  if (len(p)<6 or len(p)>20):        # Password length
      break                          # break statement
  elif not re.search("[a-z]",p):     # lowercase validation 
      break
  elif not re.search("[0-9]",p):     # number validation              
      break
  elif not re.search("[A-Z]",p):     # check for uppercase
      break
  elif not re.search("[$#@]",p):     #check for special character
      break
  elif re.search("\s",p):            #check for whitespace character
      break
  else:
      print("Valid Password")
      x=False
      break
if x:
  print("Not a Valid Password")


'''Task 2: How many vowels in your name?'''
print("***** Task 2:******")
print()
# Write a program that takes the user’s name as the input
# If there are no vowels in the name, display a message -  “You have a unique with no vowels!!”
# If vowels are present in the name, display a message -”You have a lovely name!”

import re                                             
p= input("Enter your name: ")
z=p.lower()
if not (re.search("[aeiou]",z)):
 print(" You have a unique name with no vowels")
else:
  print("You have a lovely name")


'''Task 3: This or That'''
print("***** Task 3:******")
print()
# Write a program that asks the user to input any text. The text could be a couple of words or a line or a quote.
# Your program must find if the text entered by the user has the word “this” or “that”.
import re 
pattern1="this"
pattern2="that"                                       
p= input("Enter a quote or some text: ")
q=p.lower()
if ((re.search(pattern1,q))==None):
 print("Found no 'this'")
else:
 print("Found a 'this'")
if ((re.search(pattern2,q))==None):
 print("Found no 'that'")
else:
 print("Found a 'that'")


'''Fantastic!! You are getting confident in working with in-built Python modules/packages. Way to go!!'''