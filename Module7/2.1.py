#Dictionaries
# A dictionary is defined by enclosing a comma-separated list of key-value pairs in curly braces ({}). 
# A colon (:) separates each key from its associated value
# In the code that you just executed, the key value pair represented is of an author and their book. 

''' Task 1: Stack it Right '''
print("****** Task 1: ******")
print()
# Mr.Bumblebee wants to create a list of books based on the genre.
# To know more, uncomment the statements below and click Run.
books={"J.K.Rowling":"Philosopher's Stone", 
          "Roald Dahl":"Matilda", 
          "O.Henry":"The Last Leaf"}
# print(books)
# print()

print('*** Find the book ***')
print()
# To access an item in the dictionary you need to specify the key.
# For example, to access the book written by Roald Dahl, you need to type:

# print(books["Roald Dahl"])
# print(books.get("Roald Dahl"))
# print()


''' Values and Keys '''
print("****** Task 4: ******")
print()
#To view all the values or keys in a dictionary 
# print(books.values()) 
#will print all the values of the dictionary librarians
# print(books.keys()) 
#will print all the keys of the dictionary librarians


print('*** Add more items***')
print()
# If you had to add the book “The Secret Seven” authored by Enid Blyton, you would type:
# books["Enid Blyton"]="The Secret Seven"
# print(books)

#Dictionaries cannot have two items with the same key. Duplicate keys will overwrite existing values.


print('*** Delete items***')
print()
# Some of the members of the library are moving to a new town.
# So they have approached Mr.Bumblebee to unsubscribe their membership.
# To remove a key-value pair from the you need to use the pop()  method.
# The pop() method removes the item with the specified key name. 

# books={"J.K.Rowling":"Philosopher's Stone", 
#           "Roald Dahl":"Matilda", 
#           "O.Henry":"The Last Leaf"}
# books.pop("Roald Dahl")
# print(books)

print(''' Clear and Delete''')
print()
#clear will empty the dictionary however it exists as empty


# myCar = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# myCar.clear()


#Delete will delete the dictonary.
# myCar = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del myCar
# print(myCar) #this will cause an error because "myCar" no longer exists.


print('''Task:  Dictonary''')
print()
#Create a new dictionary for the following Key-Value pair:
#name: John, age:11, city: DownTown, Grade: 6th

#After creating the dictionary, do the following operations:
#Update the age to 12
#Remove city and add address:DownTown 


info = {
  "name":"john",
  "age":"11",
  "city":"downtown",
  "grade":"6th"
}
info["age"] = "12"
info.pop("city")
info["address"] = "downtown"
print(info)