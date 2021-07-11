# You have just learnt how to use built-in functions with numbers.
# Let’s take a look at how to use built-in functions on strings.

'''Task 1: upper and lower '''
print("***** Task 1: ***** ")
print()

# Let us use the lower() function.
#txt="Hello, New House Owner!"
#txt1=txt.lower()
#print(txt1)

# Let us use the upper() function.
#txt2=txt1.upper()
#print(txt2)

# Here we will use the replace() function. Uncomment the statement below and execute it.
#txt3 = txt2.replace("H", "M")
#print(txt3)

#The format of replace function is as follows:
#  string.replace(oldvalue, newvalue, count). Here 
#   - oldvalue is the string to search for
#   - newvalue is the string replace the old value with
#   - count is optional and is a number specifying how many occurrences of the old value you want to replace. Default is all occurrences

# Here to split, the separator is the", ". So let us use the split() function. Uncomment the statement below and execute it.
#x = txt.split(", ")
#print(x)

'''Task 2: What's the code? '''
print("***** Task 2: ***** ")
print()
# Given below is the code to enter a new house.
# Coded password is: "Hello My Master, I am your New House."
# Write a program to do the following:
#  - Convert it into upper case
#  - Replace word “House” with “AppleTree”
#  - Split the message, where in the separator is the", ".

txt="Hello My Master, I am your New House."
txt1=txt.upper()
print(txt1)
txt2 = txt1.replace("HOUSE", "AppleTree")
print(txt2)
x = txt2.split(", ")
print(x)




'''More functions '''
# name = "gunjan"
# value ="12"
# space="  "
# print(name.isupper())
# print(name.islower())
# print(len(name))
# print(name.isnumeric())
# print(value.isnumeric())
# print(space.isspace())

# Here is a list of the functions we used in the program
# string.isupper() - The isupper() function returns True if all the characters are in upper case, otherwise False.
# string.islower() - The islower() function returns True if all the characters are in lower case, otherwise False.
# len(string) - The len() function returns the number of characters in the string.
# string.isspace() - The isspace() function returns True if all the characters in a string are whitespaces, otherwise False.
# string.isnumeric() -The isnumeric() function returns True if all the characters in the text are numeric

'''Task 3: Secret Code '''
print("***** Task 3: ***** ")
print()
# Studmonkey has set some instructions for anyone entering the kitchen: 
# - User to provide their first name and surname/last name in upper case:
# - User to provide their first name and surname/last name in upper case
# - User to provide their age. The age should be a double digit like 13, 14, 22 etc.
# - User to provide a secret code word which they will use each time they enter the kitchen. The code word should not have any space and should be in lower case


ch=input("Do you want to enter the kitchen? (y/n)")
while ch=="y" or ch=="Y":
 fn=input("Enter your first name: ")
 ln=input("Enter your last name or surname")
 if fn.isupper()==False or ln.isupper()==False:
     print("The first and last name need to be in upper case")
     break
 age=input("Enter your age: ")
 if len(age)<2 or age.isnumeric()==False:
   print("Age has to be double digit")
   break
 cdwrd=input("Enter and set your secret code word you will use to enter the kitchen: ")
 if cdwrd.isspace()==True or cdwrd.islower()==False:
   print("Code word needs to be in lower case and cannot be blank")
   break
 else:
   print("You are set to enter the kitchen") 
   break

'''Task 4: Ready for an adventure '''
print("***** Task 4: ***** ")
print()
# You are in charge of  taking in applications for the Summer Adventure workshop. You need to ensure that when applying students:
# - Enter their full name in upper case
# - Enter a valid age
# - Provide an email address and not leave it empty


print("***** Task 4: *****")
ch=input("Do you want to enter apply for the adventure camp? (y/n)")
while ch=="y" or ch=="Y":
 fn=input("Enter your first name: ")
 ln=input("Enter your last name or surname: ")
 if fn.isupper()==False or ln.isupper()==False:
     print("The first and last name need to be in upper case")
     break
 age=input("Enter your age: ")
 if age.isnumeric()==False:
   print("Age has to be a number")
   break
 addr=input("Enter your email address: ")
 if len(addr)==0:
   print("Email address cannot be left blank")
   break
 else:
   print("Thank you for enrolling for the adventure camp. We will share the details shortly") 
   break
