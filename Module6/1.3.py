#keyword arguments
#We can specify argument name with the value so that caller does not have to remember order of parameters.

''' Task 1:  Order of parameters '''
print("***** Task 1: *****")
print()

# def studentDetails(name,ID, age, city, school):
#   print("Student's name is ", name)
#   print(name, "'s' ID is ", ID)
#   print(name, "'s' age is ",age)
#   print(name, "'s' resides in ", city)
#   print(name, "'s' studies in ", school )

#Call the function


#In the above way, we have to remember the order of parameters.

#studentDetails(name="Michael", age=12, city="NY", ID=1234, school="Sommerville")

''' Task 2:  Variable arguments '''
print("***** Task 2: *****")
print()
#We can also pass varying number of arguments to the function
# def myFun(*argv): 
#     for arg in argv: 
#         print (arg)

# print("Result of * args: ")
# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


#Can also pass varying number of arguments through keywords using double star
# def myFun2(**kwargs): 
#     for key, value in kwargs.items():
#         print ("% s == % s" %(key, value))


# print("\nResult of **kwargs")
# myFun2(first ='Geeks', mid ='for', last ='Geeks') 

''' Task 3:  Variable arguments '''
print("***** Task 3: *****")
print()
#Write a function that take **kwargs (all integers and min 5 numbers) and find their average


'''Task4: Global vs Local Variables'''
print("***** Task 4: *****")
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
