#Real Life Problems

'''Task 1:  Delivery Charges'''
print("***** Task 1: *****")
print()
# Math πrate next quest is to take care of Building Materials Delivery
# He was asked to  create a program that takes the following input from the user:
# - The total number of sand sack and cement sack 
# -  Weight of each sack [Hint: use for loop to get the weight]
# - Use a variable to which the weight of the sack gets added as entered [Hint: calculate this within the for loop]
# - Calculates the total cost if each sack cost INR 300 [ outside the for loop]
# So let's get started

print()
tot=0
n = int(input("Enter the total number of sand and cement sacks : "))
for i in range(n):
 print("Weight for sack",i+1)
 wt=float(input("Enter the weight of the sack :"))
 tot=tot+wt
price=n*300
print("The total weight of the sacks is: ",tot) 
print("The total price to be paid is: ",price)


'''Task 2:   Lets go Outdoors'''
print("***** Task 2: *****")
print()
# Math πrate has been given the task of writing a program that takes care of outdoor field trips for kids.
# The program needs to:
# - Take the total number of kids (Number cannot be more than 8)
# - Get the name, and address for each kid
# The program must display the total cost for the field trip where
# - Cost for food for each kid is INR 500
# - Cost for travel for each kid is INR 1000
num=int(input("Enter the total number of kids coming for the trip"))
if num>8:
 print("Trip cannot have more than 8 kids")
else:
 for i in range(num):
   name=input("Enter the name of the kid: ")
   addr=input("Enter the address: ") 
 print("Total cost for the food: ",num*500)
 print("Total cost for the travel: ",num*1000)


