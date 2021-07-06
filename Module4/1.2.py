#Lets learn using for loop along with strings
'''Task 1: Get Looping '''
print("**** Task 1: ****")
print()
# Using a for loop, print out each individual character in a string. 
# Uncomment the statements below and click on Run
#text = "Looping"
#for c in text:
# print(c)
# What if you want to display the characters, next to each other separated by a comma like:
# L,o,o,p,i,n,g
# For this all you need to do is add the following code in the print # statement like:
# print(c,end=",")


'''Task 2: Character Delimiter '''
print("**** Task 2: ****")
print()
#Use for loop and seperator to print alphabets in your name seperated by any special charaacter.
name=input("Enter your name: ")
for c in name:
 print(c,end="@")
 print(c)


'''Task 3: Find me if you can '''
print("**** Task 3: ****")
print()
# Write a program that takes the following input from the user:
# Any word, for example, plant
# A character to search in the word 
# The program needs to display the number of occurrences of the character searched for. [Hint: Use a counter variable]
# Now try the program by inputting a sentence and then searching for a character
# Did it work?
ctr=0
name=input("Enter a word: ")
c=input("Enter the character to search in the word: ")
for i in name:
 if i==c:
   ctr=ctr+1
print("The number of occurrences of the character ",c," is ",ctr)

'''Task 4: You’ve got a mail '''
print("**** Task 4: ****")
print()
# write a program that asks the user to enter the email address for a promotional fun event
# The program needs to check if the email address entered is valid.[Hint: check if the user has used the character “@” only once] 
ctr=0
name=input("Enter the email address: ")
for i in name:
 if i=="@":
   ctr=ctr+1
if ctr==1:   
   print("Valid email address")
else:
   print("Invalid email address")