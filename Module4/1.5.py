#break vs continue
# Use of break statement inside the loop

'''Task 1:  Break vs continue'''
print()
print("***** Task 1: *****")
print('***Break***')
#Uncomment the following code to observe Break
#The program is to find the first occurance of 'e'

# count=0
# for val in "believe":
#   count=count+1
#   if val == "e":
#     break
    
# print("i is present at ", count, " index")

print()
print('*****continue*****')
#Following is the program to print all occurance except 'e'

# for val in "believe":
#   if val == "e":
#       continue
#   print(val)

'''Task 2:  Break '''
print()
print("***** Task 2: *****")
print('***Break***')
#Write a program to find all prime numbers between 2 and 10.
for i in range(2,11):
  count = 0
  for j in range(2 , i):
    if i % j == 0:
      print(i, " is Not A Prime Number")
      break
    else:
      count = count + 1 
  if(count== i-2):  
    print(i," is a Prime Number")      


''' Task 3: To continue or not '''
print("***** Task 3: *****")
print()
# Write a program using the for loop to print all the numbers between 1 to 100, except the multiple of 5 