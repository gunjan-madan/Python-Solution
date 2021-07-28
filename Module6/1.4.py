

'''Task1: Global vs Local Variables'''
print("***** Task 1: *****")
print()
#Global variables are the ones that are defined and declared outside any function and are not specified to any function. They can be used by any part of the program.
#Local variables are specific to a particular function
# This function has a variable with 
# name same as s. 

# def f():  
#     s = "Me too."
#     print(s) 
    
# # Global scope 
# s = "I love python" 
# f() 
# print(s)

'''Task1: Global keyword'''
print("***** Task 1: *****")
print()

# global keyword allows you to modify the variable outside of the current scope. 

# The basic rules for global keyword in Python are:

# When we create a variable inside a function, it is local by default.
# When we define a variable outside of a function, it is global by default. You don't have to use global keyword.
# We use global keyword to read and write a global variable inside a function.
# Use of global keyword outside a function has no effect.

# def f():  
#     global s
#     #s="me too"
#     print(s) 
    
# # Global scope 
# s = "I love python" 
# f() 
# print(s)



'''Task 2: Lets get global'''
print("****** Task 2: ******")
print()
# Create a program that:
# - Declares a global variable called balance, and assign a value to it
# - Write a function that :
# --> Takes an input value from the user and adds it to the balance. 
# --> Displays the updated balance value
# - Use a for loop, to call the function thrice.


balance=3000
def tot(val):
 global balance
 balance=balance+val
 return(balance)
for i in range(3):
 num=int(input("Enter value to add to balance: "))
 print("The updated balance is:",tot(num))