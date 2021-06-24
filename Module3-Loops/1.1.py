# Sam, your friend wants to print his dog's name,Snoopy, five times.
# He asks you to help him, as you are learning to code in Python
# Can you help him?
'''Task 1: Repetition'''
print("**** Task 1: ****")
print()
# One of the ways is to use 5 print statements like this:
print ("Snoopy")
print ("Snoopy") 
print ("Snoopy")
print ("Snoopy")
print ("Snoopy")
#Better way is to use while loop
# The structure of the while loop is:
''' while <condition>:
      code to be repeated
      code to be repeated
    Code outside the loop '''
# Uncomment the next 4 lines to see the while loop in:
#counter = 1      	         # initialize a counter variable
#while counter <= 5:       # loop condition
 #print("Snoopy")  	   # code to execute
 #counter = counter + 1


'''Task 2: Print While You Can'''
print("**** Task 2: ****")
print()
# Sam is having fun learning with you. He wants  you to write a program to print the first 100 numbers.
# Can you do that? 
print("**Printing the first hundred numbers**")
counter = 1      	    
while counter <= 100:       
 print(counter)   	  
 counter = counter + 1  

#Also find total of first hundred numbers
print("**Printing the sum of first hundred numbers**")
counter = 1   
total=0  	    
while counter <= 100: 
  total=total+counter  
  counter = counter + 1
print("The total is: ",total)


'''Task 3: Print Within Limits'''
print("**** Task 3: ****")
print()
# The previous task has made Sam interested to write a program where he can find the sum of numbers from 1 to a number that the user wants. Can you help him?
# Hint: You can take that limit as input from the user, every time the program runs
limit=int(input("Enter the number till which the sum needs to be calculated: "))
counter = 1   
total=0  	    
while counter <= limit:   
 counter = counter + 1
 total=total+counter
print("The total is: ",total)




'''Task 4: Reverse Printi'''
print("**** Task 4: ****")
print()
# Sam is really loving the way he is able to play with numbers using the while loop.
# He now wants to understand if he can do a reverse printing of numbers i.e.backward counting
# He wants you to write a program that will print the first 50 numbers backwards.
# Hint: Instead of assigning 0 to the counter, set it to 50, and decrement the counter(i.e. subtract by 1)
counter = 50   	    
while counter >= 1:
 print(counter)  
 counter=counter - 1