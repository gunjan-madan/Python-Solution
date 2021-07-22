'''Task 1: What's the codeword?'''
print("****** Task 1: *******")
print()
# Mr.Beaver has kept a list of codewords for entry into his house
# Whoever guesses the code words at the entrance gate, is allowed to enter his house.
# The list of code words are:rainbow, butterfly, sunshine,cupcake
# Create a list of above codewords
# Take an input codeword from user
# Check if that matches from the list. If it matches, person can enter otherwise not
codewords=["rainbow", "butterfly", "sunshine","cupcake"]
guestcdwrd=input("Enter the codeword: ")
for i in codewords:
 if guestcdwrd.lower()==i:
   print("The codeword is right. You may enter.")
   break;
else:
 print("Sorry. Incorrect Password")


'''Task 2: Earn Your Brownie Points'''
print("****** Task 2: *******")
print()
# Mr.Beaver and his family visit the gym regularly. 
# There are four members in his family - Otto, Beth, Bob, Emma
# To ensure that each of them gets to exercise, Mr.Beaver has put a brownie points tally.
# The scores are calculated as follows:
# The brownie points are calculated at the end of the week and each one gets a goodie package, based on their score.
# 5 brownie points for exercising 1 to 3 hrs
# 10 brownie points for exercising 4 to 6 hrs
# Anything more than 6hrs, you get 15 brownie points.
# Can you help Mr.Beaver write a Python program that calculates the brownie points earned by each member in a week.
# Mr.Beaver wants a list that displays the name of the family member, hours worked and brownie points earned.
# For example [Otto, 3,5,Beth,5,10, Bob, 2,5,Emma,7,15]
score=[]
bpoints=0
family=["Otto","Bob","Bert","Emma"]
for i in family:
 print("Hi ", i)
 hrs=float(input("Enter the number of hours you worked in the gym: "))
 if hrs<=3:
   bpoints=5
 elif hrs>=4 and hrs<=6:
   bpoints=10
 else:
   bpoints=15   
 score.append(i)
 score.append(hrs)
 score.append(bpoints)
print(score)


'''Task 3: Let’s string them together'''
print("****** Task 3 : *******")
print()
# Mr.Beaver owns a poultry farm where he packs and supplies eggsHe packs in multiples of 5 or 10.
# So the orders for Eg. are: 10 packs of 5 eggs  or 8 packs of 10 eggs.
# The cost is then calculated as $2 per egg.
# The list consisting of the following items is then shared with the customer: [name of the customer, total number of eggs,total cost]
# Write a program to help Mr.Beaver generate the list.
# Remember your program should allow for more than one customer entry.


custdetails=[]
exitch=""
while(exitch.lower()!="exit"):
 custname=input("Enter your name: ")
 pack=int(input("What type of packaging do you need:\n 1.Pack of 5\n 2.Pack of 10?\n"))
 noofPacks=int(input("How many packs do you want ? "))
 if pack==1:
     toteggs=5*noofPacks
 else:
   toteggs=10*noofPacks
 totcost=toteggs*2
 custdetails.append(custname)
 custdetails.append(toteggs)
 custdetails.append(totcost)
 exitch=input("Do you want to enter another customer details?\nPress Enter to continue or Exit to stop")
print(custdetails)