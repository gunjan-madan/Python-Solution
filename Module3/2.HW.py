# Have you had to stand in a queue at a billing counter, when you just had to bill for two items? 
# Well, what if we had an express billing counter, wherein one could bill for 10 or less items 
# Shall we create a program to do this?
'''Task 1: Calmart Express Counter'''
print("**** Task 1: ****")
print()
# You work at the Express Cash Counter of Calmart Store
# At the Express Cash counter, you are allowed to check out only 10 items.
# Your program needs to :
# - Let the customer know the total price as each item is added
# - Allow price of only 10 items
# - Display the total amount the customer has to pay for the 10 items purchased
print("**** Task 1: ****")
ctr=0
tot=0
while(ctr<=10):
 price=float(input("Enter the price of the item: "))
 tot=tot+price
 ctr=ctr+1
 if ctr==10:
   break
 else:
   print("Your total price so far is: ",tot) 
print("Total price to pay: ",tot)


'''Task 2: Cookie Time'''
print("**** Task 2: ****")
print()
# You have decided to bake cookies for your friend
# You have to warm the oven to 350 degrees
# The starting temperature for your oven is 120 degrees
# It takes about 2 mins for the temperature to increase by 10 degrees
# You want to write a program, that gives you the time it will take to reach the final temperature
start_temp=110
tm=0
while start_temp <=320:
 start_temp=start_temp+10
 tm=tm+2
 if start_temp==320:
   break 
print("The final temperature is: ",start_temp)
print("The time taken to reach the temperature is: ",tm)


