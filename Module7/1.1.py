#List

'''Task 1: Lists'''
print("******Task 1: ******")
print()
#  A list is a number of items or names written or grouped together. 
# If you want to access any of the items in  the list you will need to use something called the index, which is the position of the item in the list. 
# Note that the position of the item starts with 0
#For example:

# fruits = ["Banana", "Kiwi", "Apple", "Grapes"]
# print(fruits)
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[3])

'''Task- Use For Loop'''
# Can you change the code to print the list of fruits using a for loop?

'''Task 2:  Grocery Dam'''
print("****** Task 2: *****")
print()
# Mr.Beaver wants you to get the following items from the Supermarket:
# Bakery Items: Bread, Bagels, Muffins, Cookies, Croissant
# Vegetables: Lettuce, Spinach, Carrots, Corn, Tomato
# Can you create a separate Python list for the bakery items and vegetables, and display the output?
bakery = ["Bread", "Bagels", "Muffins", "Cookies", "Pastries"]
vegetables=["Lettuce", "Spinach", "Carrots", "Corn", "Tomato"]
print("Bakery \t\t Vegetables")
print("-------      ----------")
for i in range(5):
 print(bakery[i],"  \t",vegetables[i])

''' Task 3: Changes to a list '''
print("***** Task 3: *****")
print()
print("***Replacing an item in a list***")
spaceobj=["rocket","planet","asteroid"]
#spaceobj[1]="alien"
#print(spaceobj)
#print()
print("***Adding an item to the end of the list***")
#spaceobj.append("moon")
#print(spaceobj)
#print()
print("***Deleting an item to the list***")
#del spaceobj[1]
#print(spaceobj)
print('***Count of particular item in a list***')
#print(spaceobj.count("rocket"))
#print(spaceobj.count("alien"))
print('***Insert at a particular index***')
# spaceobj.insert(2,"rock")
# print(spaceobj)

'''Task 4: More to append'''
print("***** Task 4: ******")
print()
# In the lists created in Task 2, add cabbage at index 2 and potato at the end to the vegetable list. Remove “Bagel”  from the bakery list.
# vegetables.insert(2,"cabbage")
# vegetables.append("potato")
# print(vegetables)
# del bakery[1]
# print(bakery)