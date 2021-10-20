#keyword arguments
#We can specify argument name with the value so that caller does not have to remember order of parameters.

''' Task 1:  Order of parameters '''
print("***** Task 1: *****")
print()

def studentDetails(name,ID, age, city, school):
  print("Student's name is ", name)
  print(name, "'s' ID is ", ID)
  print(name, "'s' age is ",age)
  print(name, "'s' resides in ", city)
  print(name, "'s' studies in ", school )

#Call the function
# studentDetails("Namith", "6435", "11", "")

#In the above way, we have to remember the order of parameters.

# studentDetails(name="Namith", age=11, city="APEX", ID=6475, school="Peak Charter Academy")

# ''' Task 2:  Variable arguments '''
# print("***** Task 2: *****")
# print()
# #We can also pass varying number of arguments to the function
# def myFun(*args): 
#     for arg in args: 
#         print (arg)

# print("Result of * args: ")
# myFun('Hello', 'Welcome', 'to', 'Python')

''' Task '''
#Write a function that take **args (all integers and min 5 numbers) and find their average
def average(*integers):
  value=0
  for integer in integers:
    value = integer + value
  avg = value/len(integers)
  return avg

result=  average(10,20,30,40)
print(result)


''' Task 4:  Variable arguments with Keywords '''
print("***** Task 4: *****")
print()
#Can also pass varying number of arguments through keywords using double star
def myFun2(**kwargs): 
    for key, value in kwargs.items():
        print(key, "==", value)
        # print ("% s -- % s" %(key, value))


print("\nResult of **kwargs")
myFun2(first ='Coding', mid ='Is', last ='Interesting') 


''' Task '''
#Write a function that take **kwargs 
#Take five numbers input from user, send it to function using **kwargs with their keywords (First, Second, Third, Fourth, Fivth)
#Find the maximum and print the number along with the keyword
def findMax(**nums):
  maxNum = 0
  maxKey = ''
  for key, value in nums.items():
    if value > maxNum:
      maxNum = value
      maxKey = key
  print("The maximum of all numbers is ", maxNum , " at ", maxKey, " position")



# Maximum of all numbers is 43 at third position
findMax(I = 12,II= 1132,III = 143,IV=100,V=19)

#Write a function to find all even numbers along with their position
# def even(**evens):
#   for key, value in evens.items():
#     if value % 2 == 0:
#       print(value, key)

    
# even(I = 12, II = 15, III = 18, IV = 68, V = 47)
    
    
    
# even(first= 11, second=22, third=33)