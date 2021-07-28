# A tuple is a collection which is ordered and unchangeable.
# In Python, data in a tuple is written within round brackets and assigned to a variable. 

''' Task 1:  All about tuples '''
print("***** Task 1: *****")
print()
# To access tuple items, you specify the  positional index number, inside square brackets.
# mytuple = ("red", "blue", "green")
#for i in range(3):
# print("Element ",i," is",mytuple[i])



''' Task 2:   Code assignment '''
print("***** Task 2: *****")
print()
# Mr.Ante has unique code consisting of numbers and words.
# He assigns this code to new employees who join his organization.
# Here is the list of the codes: 
# "ap089", "ba42n", "ch67ry", "78ange", "ki612", "mel303", "458go"
# He wants you to write a program to:
# - Store the code in a tuple
# - Get the name of the new employee as input
# - Randomly assign a code from the tuple to the new employee [Hint: Use the random.choice() function]

import random
mytuple = ("ap089", "ba42n", "ch67ry", "78ange", "ki612", "mel303", "458go")
name=input("Enter your name: ")
print("Hi ",name,"\nThe code assigned to you is :", random.choice(mytuple))


''' Task 3: Code (Dis)organized '''
print("***** Task 3: *****")
print()
# Mr.Ante wants to change the code "mel303" to "ben405". 
# He has written the code and wants to check if it works. 
# Uncomment the statements and observe the result.

#mytuple[5]="ben405"
#print(mytuple[5])

# What did you observe?
# You cannot change its values. Tuples are unchangeable.

# Here is a workaround. Uncomment the statement below and click Run.

#y = list(mytuple)
#y[5] = "ben405"
#mytuple = tuple(y)
#print(mytuple)

# Here we use the swapping technique. 
# - First convert the tuple into a list
# - Make change to the value in the list
# - Convert the list back into a tuple

''' Task 4: Codify '''
print("***** Task 4: *****")
print()
# Mr.Ante has been given 5 additional code to add.
# Here are the codes:
# "we342","kl782","pr907","sh149"
# Before adding the code: 
# - Check the number of items in the tuple.
# - If the number of items is less than 10, add the codes
# - If the number of items is more than 10, create a new tuple to add the items. 
# Hint 1: Use len() function to find the number of items. For ex:len(mytuple)
# Hint 2: Use swapping technique (shown in previous task) to add items
if len(mytuple) >10:
 newtuple=("we342","kl782","pr907","sh149")
else:
 ctr=0
 newtuple=("we342","kl782","pr907","sh149")
 length=len(mytuple)
 y = list(mytuple)
 for i in range(length+1,length+5):
   y.append(newtuple[ctr])
   ctr=ctr+1
 mytuple=tuple(y)
print(mytuple)


''' Task 5: Present or absent '''
print("***** Task 5: *****")
print()
# Uncomment the statements below and click Run

#x = mytuple.count("pr907")
#print(x)

# What did you observe? 
# count() function returns the number of occurrences of a search string.
# Mr.Ante wants you to write a program that
#  - Takes the input code from the user
#  - Checks if it is already present in the tuple
#  - Displays a message “Already available, if present

srch=input("Enter code to search: ")
cntx=mytuple.count(srch)
if cntx >=1:
 print(srch," is already available in the tuple")
else:
 print(srch," not available in the tuple")