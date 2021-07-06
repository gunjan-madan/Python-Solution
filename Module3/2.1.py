#while loop along with if conditions

# Have you been to a game arcade? 
# Which of the games are your favourite? 
# Are you ready to design one?
''' Task 1: Number Buzzer Game'''
print("**** Task 1: ****")
print()
# Write a “Guess the Number”  game, where a player has to guess a number between 10 and 20.  Let's assume that the number to guess is 15.
# Let's add some checks to the game, you have written:
# If the number is lesser than 10, you must give a warning message and ask them to guess again
# If the number is greater than 20, you must give a warning message for the same and ask them to guess again
# If the number is right, then you display a congratulatory message
num=int(input("Guess a number between 10 and 20: "))
while(num!=15):
 if num<10:
   print("Number is lesser than 10")
   num=int(input("Guess a number between 10 and 20: "))
 elif num>20:
   print("Number is greater than 20")
   num=int(input("Guess a number between 10 and 20: "))
 else:
   print("Try again!!")
   num=int(input("Guess a number between 10 and 20: "))
print("Bingo!! You guessed right")

''' Task 2: Break the loop'''
print("**** Task 2: ****")
print()
# Now let's bring in a twist in the program you wrote in Task 1. # You need to modify the program, in a way that it allows only 3 chances to guess the number.
ctr=1
while(ctr<=3):
  num=int(input("Guess a number between 10 and 20: "))
  if num<10:
    print("Number is lesser than 10")
  elif num>20:
    print("Number is greater than 20")
  elif num==15:
    print("Bingo!! You guessed right!")
    break
  else:
    print("Try again!!")
  ctr=ctr+1

  ''' Task 3: To quit or not to quit'''
print("**** Task 3: ****")
print()
# Write a program that takes numbers between 1 and 100 from the user.
# To quit entering numbers the user needs to press 0. 
# The program should then display the sum and the product of the numbers.
print("**** Task 3: ****")
num=1
tot=0
prod=1
while(num!=0):
 num=int(input("Enter a number (To quit press 0: )"))
 if num < 0 or num > 100:
  print("Enter a number between 1 and 100")
 elif num==0:
   break 
 else:
   tot=tot+num
   prod=prod*num  
print("Sum: ",tot)  
print("Prod:",prod)