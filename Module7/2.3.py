#Grouping Multiple values by same key

print('*** Multiple books by one author***')
print()
#If there are multiple books by authors and you want to group them together.
# Uncomment the statements below and click Run.
# bookdetails={"SN1":["Dr.Seuss","The Cat in the Hat"],
#             "SN2":["E. B. White","Charlotte's Web"]}
# print(bookdetails["SN1"])


print('*** Task: Groups***')
print()
# Write a program to create a dictionary of library members as given in the format(ID,Name,Phone number):
# MN012,Beth,9823628678
# MN890,Noah,9710234573
# MN456,Tia,9563029266
# MN347,Sean,9025394528
# Your program should print the details of all the members
# Hint: Assign a set of values to the membership number
members={"MN012":{"Beth","9823628678"},
        "MN890":{"Noah","9710234573"},
        "MN456":{"Tia","9563029266"},
        "MN347":{"Sean","9025394528"}}
print("***** Details of all the Members *******")
print(members)


''' Task 2:  Add to the Stack '''
print("****** Task 2: ******")
print()
# Mr.Bumblebee now has to add details of four more members to the list.
# To add items to the list, you need to specify the dictionary name, followed by the key, and the value(s). 
# Here is an example to add details of a person named Nita to the members dictionary:
#members["MN598"]="Nita","9870987677"
# Write a program to add the following details to the members dictionary
# MN908,Mita,9870987699
# MN231,Sandra,9578091872
# MN616,Ayur,9109725534
# MN990,Sara,9320997486
# Once you have added the members, create a copy of the dictionary.
# A copy of the dictionary can be created using the copy() function
# For example:
#membercopy=members.copy()
members["MN908"]="Mita","9870987699"
members["MN231"]="Sandra","9578091872"
members["MN616"]="Ayur","9109725534"
members["MN990"]="Sara","9320997486"
print("*** List of Members ***")
print(members)
membercopy=members.copy()


''' Task 3: Pop Hop '''
print("****** Task 3: *******")
print()
# Some of the members of the library are moving to a new town.
# So they have approached Mr.Bumblebee to unsubscribe their membership.
# For example to remove a member with the key MN234: 
#members.pop("MN234")
# You need to write a program to remove the following library members: 
# Beth -> Membership Number: MN012
# Ayur -> Membership Number: MN616
# Check the length of the dictionary after removing the members. [Hint: Use the len() function]
print("*** List of Members ***")
print("Number of members before deletion: ",len(members))
members.pop("MN012")
members.pop("MN616")
print("Members after removal:")
print(members)
print("Number of members after deletion: ",len(members))



''' Task 4: Merge to Surge '''
print("****** Task 4: ******")
print()
# Mr.Bumblebee wants you to create two dictionaries - 
#  1. Details of the different library sections.
#  2. Membership Detail
# Here are the details of the different library sections:
# - Acquisition Section - Receives requests  for new books
# - Classification Section - Subject wise classification of books
# - IT Section - Provides automated,digital Library Service
# - Reference Section - Consists of encyclopaedias, and reference books
# Here are the details of the membership types:
# - Full - Full access to the Library Services
# - Associate - Borrowing rights 
# - Remote - Access to Digital Services
# Mr.Bumblebee then wants you to combine these two dictionaries into one called  Library Details. To combine dictionaries you need to specify it as:
#newdictionary={“Key1”:dictionary1,
#               “Key2”:dictionary2}

libsection={"Acquisition Section":"Receives requests for new books",
          "Classification Section":"Subject wise classification of books",
          "IT Section":"Provides automated,digital Library Service",
          "Reference Section":"Consists of encyclopaedias, and reference books"}
print()          
print("**** Library Sections *****")
print(libsection)
#Membership Details
libmembership={"Full":"Full access to the Library Services",
               "Associate":"Borrowing rights",
               "Remote":"Access to Digital Services"}
print()
print("***** Membership Details ******")
print(libmembership)
#Combined Dictionary
libdetails={"Section":libsection,"Membership":libmembership}
print()
print("***** Combined Dictionary ******")
print(libdetails)