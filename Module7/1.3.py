'''Task 1: Unique Identifier'''
print("****** Task 1: ******")
print()
# Mr.Beaver's poultry business is doing very well.
# He now realizes that he needs to create a unique ID for each of the livestock in his farm.
# He wants you to create a program where the ID generated will have:
# - The current year
# - A random selection of colour code [Colour codes to be used are:red,blue,pink,yellow]
#- A randomly generated number between 1 and 100
# - A random selection of special characters (Special characters to be used are: $,#,@,!) 
import datetime
import random
color=["red","blue","pink","yellow"]
spchar=["$","#","@","!"]
dt = datetime.datetime.now()
d=str(dt.year)
#random pick of colour
z=random.choice(color)
#random pick of special character
y=random.choice(spchar)
x=str(random.randint(1,100))
print(d)
print(z)
print(y)
print(x)
uid=d+y+x+z
print("The unique ID generated is: ",uid)


''' Task 2: Duplicate or not '''
print("****** Task2: ******")
print()
# Mr.Beaver has an initial list of furnitures to buy and is still adding to the list
# To avoid duplication, he wants you to write a program that detects if the item already exists in the list  
# If the item exists, display a message saying "Item exists"
# If the item does not exist, append the item to the list and display the entire list
# The existing list has the following items:  tables, chairs, bed, dresser

items=["tables", "chairs", "bed", "dresser"]
print("**** List of Items*****")
newitem=input("Enter the item: ")
newitem=newitem.lower()
present=0
for i in items:  
 if i==newitem:
   present=1
   break
 else:
   present=0
   break

if present==1:
  print("Item exists")
else:
  print("Item does not exist")  

print("Here is the list of items:\n",items)
