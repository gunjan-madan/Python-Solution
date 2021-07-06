
''' Task 1: Numerical Trial '''
print("**** Task 1: ****")
print()
# The first stage of the quest is a trial run. 
# The quest is asking you to analyze and observe the program output.
# Uncomment the statements below and click Run

#for i in range(15):
#  if (i % 2) == 0:
#    print(i,"is a even number")
#  else:
#    print(i,"is a odd number")

# The range() function, takes three arguments: range(start, stop, step)
#start and step and optional parameters.

# Uncomment the statement below and click Run:

#x=0
##define a while loop
#while(x <4):
#  print(x)
#  x = x+1
##Define a for loop 
#for x in range(4):
# print(x)


'''Task 2: Who is the odd one out'''
print("**** Task 2: ****")
print()
# Math πrate is ready to take the next small steps in the coding quest. 
# Write a program that prints the odd numbers that occur between the 10 and 20

for i in range(10,20):
 if (i % 2) != 0:
   print(i)




'''Task 3: Ready to Skip'''
print("**** Task 3: ****")
print()
# Do you remember the program that you wrote on skip counting? 
#Take three inputs from user: starting number, ending number and skip interval.
#Print respective numbers
numstart = int(input("Enter the starting number: "))
numend=int(input("Enter the ending number: "))
cnt=int(input("Enter the skip count number: "))
for i in range(numstart,numend,cnt):
 print(i)


'''Task 4: Sum and Product'''
print("**** Task 4: ****")
print()
# Math πrate is very happy with your help. 
# You need to assist Math πrate in writing a program that takes a starting and ending number and then calculates the:
# Total sum of the numbers between the starting and ending number
# Product of the numbers between the starting and ending number
tot=0
prod=1
numstart=int(input("Enter the starting number"))
numend=int(input("Enter the ending number"))
for i in range(numstart,numend):
 tot=tot+i
 prod=prod*i
print("The sum of the numbers is: ",tot)
print("The product of the numbers is: ",prod)

'''Task 5: Lets get Even'''
print("**** Task 5: ****")
print()
# Math πrate has been working with each of the coding quest tasks effortlessly with your help.
# He has been given another number based quest.
# He needs your help in writing a program that takes :
# A starting and and ending number as the input from the user
# For each number between that range:
# If the number is an even number, then the output must display the square of the number
# If the number is odd, then the output must display the cube of the number
# Are you ready to help him with the program? 
numstart=int(input("Enter a starting number: "))
numend=int(input("Enter the ending number: "))
for i in range(numstart,numend):
 if i%2==0:
   sq=i*i
   print("Square of the even number: ",sq)
 else:
   cu=i*i*i
   print("Cube of the odd number: ",cu)