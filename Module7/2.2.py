#Nested Dictionaries
#A nested dictionary is a dictionary inside a dictionary. It's a collection of dictionaries into one single dictionary.

# nested_dict = { 'dictA': {'key_1': 'value_1'},
#                 'dictB': {'key_2': 'value_2'}}
print()
print('***Example of Nested Dictionary***')
print()

familyMembers={1:{'name': 'John', 'age':'27', 'gender':'Male'},
               2:{'name': 'Susan', 'age':'15', 'gender':'Female', 'hobby': 'painting'}}
print(familyMembers)

print()
print('***Access elements')
print()
# print(familyMembers[1])
# print(familyMembers[1]['name'])
# print(familyMembers[1]['age'])
# print(familyMembers[1]['gender'])

print()
print('***Add New elements to the dictionary***')
print()
# familyMembers[3]={}
# familyMembers[3]['name'] = 'Luna'
# familyMembers[3]['age'] = '24'
# familyMembers[3]['gender'] = 'Female'
# familyMembers[3]['married'] = 'Yes'
# print(familyMembers[3])

#You can directly asssign a dictionary also
# familyMembers[4] = {'name': 'Peter', 'age': '29', 'gender': 'Male', 'married': 'Yes'}
# print(familyMembers[4])

print()
print('***Iterate through the nested dictionary***')
print()
# for p_id, p_info in familyMembers.items():
#     print("\nPerson ID:", p_id)
    
#     for key in p_info:
#         print(key + ':', p_info[key])

print()
print('***Delete Items from Dictionary***')
print()
#To delete one specific Item:
# members = {1: {'name': 'John', 'age': '27', 'gender': 'Male'},
#           2: {'name': 'Marie', 'age': '22', 'gender': 'Female'},
#           3: {'name': 'Luna', 'age': '24', 'gender': 'Female', 'married': 'No'},
#           4: {'name': 'Peter', 'age': '29', 'gender': 'Male', 'married': 'Yes'}}

# del members[3]['married']
# del members[4]['married']
# print(members)

# Delete entire nested dictionary
# del members[4]
# print(members)

''' Task 1: Stack it Right '''
print("****** Task 1: ******")
print()
#Create a nested dictonary for icecreams and display result like:

# Ice Cream: 0
# flavor: Vanilla
# price: 0.5
# pints: 20
# Ice Cream: 1
# flavor: Chocolate
# price: 0.5
# pints: 31
# Ice Cream: 2
# flavor: Cookies and Cream
# price: 0.75
# pints: 14


icecream = {0 : {"flavor" : "Vanilla", "price" : "0.5", "pints" : "20"}, 1 : {"flavor" : "Chocolate", "price": 0.5, "pints" : "31"}, 2 : {"flavor" : "Cookies & Cream", "price" : "0.75", "pints" : "14"}}
print(icecream)

for numb, cream in icecream.items():
  print("\nIcecream: ", numb)

  for key in cream:
    print(key + ":", cream[key])
