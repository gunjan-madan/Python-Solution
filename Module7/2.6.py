# Mr.Beaver and Mr.Bumblebee have opened a farm market.
# They need your help for the following tasks:
# Task 1: Create inventory stock of items
# Task 2: Create the price list for the items
# Task 3: Get the shopping list
# Task 4:Create a function that generates the bill. The bill should take into consideration
# - Checking the inventory stock 
# - Checking the price list

'''Task 1: Create Inventory Stock'''
print("****** Task 1: ******")
print()
# Create a dictionary with items and their stock.
# You can start with the following items:
# Banana - 10
# Apple - 15
# Orange - 32
# Pear - 15
# Print the stock after creating the dictionary
#create stock
stock = {
   "banana": 10,
   "apple": 15,
   "orange": 32,
   "pear": 15
}
print("*** Stock ***")
print(stock)

'''Task 2: Create the price list'''
print("***** Task 2: *****")
print()
# Create a dictionary that stores the price for the items.
# Here is the price for the items:
# Banana - 20
# Apple - 80
# Orange - 60
# Pear - 90
#create pricelist
price={"banana":20,
     "apple":80,
     "orange":60,
     "pear":90}
print("***** Price List******")
print(price)

'''Task 3: Getting the Shopping List'''
print("***** Task 3: *****")
print()
# Write the code to get the quantity of each item from the user.
# If the user does not want a particular item, they need to enter 0.
# Hint: Create a copy of the item list and get the user to enter the quantity for each item.
#shoplist

shoplist=stock.copy()
for i in shoplist:
 print("Specify quantity for",i)
 print("Type 0 if item not required:")
 shoplist[i]=int(input("Enter quantity: "))  
print("Your shopping list is:\n",shoplist)

'''Task 4: Compute the Bill'''
print("***** Task 4: *****")
print()
# Create a function to calculate the total price for items ordered.
# The function must:
# - Check the stock of items
# - Display the total price
#Function to compute total
def computeprice(stklist):
 total=0
 for i in stock:
   if stock[i]>=stklist[i]:
     total=total+stklist[i]*price[i]
   else:
     print(i," is out of stock")
 print ("The total amount to be paid is: ",total)
 
# Compute Bill
computeprice(shoplist)

'''Brilliant!! You have automated the inventory related tasks.. Awesome!!'''