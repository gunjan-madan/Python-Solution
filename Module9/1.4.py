# Lambda functions can be used to return values based on conditional logic.
# This is done using the if- else statement in a lambda function.
# Let's take a look.

'''Task 1:  Check the conditions'''
print("***** Task 1: *****")
print()
# Uncomment the statement below and click Run
#lambdatest = lambda x: x*2 if x < 3 else x
#num = 72
#print(lambdatest(num))
# What did you observe?
# In the above code snippet, the lambda function checks if the number passed as an argument is lesser than 3
# If yes, then the number passed as the argument is multiplied by 2
# If not, then the number is returned as is.
# Write a program to :
# - Take the number as an input from the user.
# - Check if the number is divisible by 3. If yes, multiply the  number with 5, else multiply the number with 3. 

# num= int(input("Enter the number: "))
# divisible_3= lambda x: x*5 if x%3==0 else x*3
# print(divisible_3(num))

''' Task 2: All about passwords '''
print("***** Task 2: *****")
print()
# Write a program that accepts the password from the user.
# If the password starts with a space, then ask the user to enter again.
# The user gets three chances to key in the password.
# Hint: use the function startswith() to check the password starts with a space. Here is an example of using the function:
#x="Perl"
#if x.startswith("P")==True:
#  print("Awesome")

# no_space= lambda x: False if x.startswith(" ")==True else True

# count=0
# while count<3:
#   password= input('Enter a valid password: ')
#   if(no_space(password)):
#     print("Password Accepted!")
#     break
#   else:
#     print("Sorry! Invalid Password")
#     print(2-count, " attempts left.")
#     count=count+1


''' Task 3: Filter funnel '''
print("***** Task 3: *****")
print()
# Write a program that:
# - Takes an original string consisting of numbers and alphanumeric strings. For example: str1 = "leaf 15 plant8 9 flowers7 buds 56 21shrubs 21 5"
# - Filters the numbers out of the string and stores them in a list
# - Displays the final list of numbers

# str1 = "leaf 15 plant8 9 flowers7 buds 56 21shrubs 21 5"
# str_list = str1.split(' ')
# filtered_list = list(filter(lambda x: x.isnumeric()== True, str_list))
# print("The numbers extracted from the string:\n",filtered_list)


''' Task 4: Tinker Bell '''
print("***** Task 4: *****")
print()
# “Tinker Bell” school has decided to give extra classes in Maths for students who have scored less than 60.
# Write a program that:
#  - Takes the name and marks of student 
# - Creates the list of students who would need extra classes
# - Hint 1: Use list and dictionaries 
# - Hint2: You can loop through both keys and values, by using the items() method. For example:
#for x, y in mydict.items():
#  print(x, y)
mrklst={}
finalist=[]
num=int(input("Enter the number of students: "))
for i in range(num):
 name=input("Enter name:")
 marks=int(input("Enter marks: "))
 mrklst[name]=marks
print("The list of students:\n",mrklst)


'''Great!! You are becoming a pro in using lambda functions.'''
