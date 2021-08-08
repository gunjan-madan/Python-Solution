# In one of the previous goals, you used the class design to create a banking application.
# Lets modify the program to use the exception class to handle errors. 

''' Task:   Exception Handling in Banking Application '''
print("***** Task: ******")
print()
# The banking application program using the class design has been provided.
# Use the exception class to handle the errors a user might encounter. Here are some of the scenarios where you might encounter errors:
# - Withdrawal amount is greater than balance
# - Selecting options not shown in the menu
# - Entering non-numeric data(check for ValueError)  

class MyError(Exception):
   def __init__(self,args):
     # The variable msg gets the error message to be passed
     self.msg=args
 
# Creating a class called student
class bank:
# initialize variables
 def __init__(self, custname,acctype,balance=0.0):
  self.custname=custname
  self.acctype=acctype
  self.balance=balance
 # Method/Function to add deposit amount
 def deposit(self,amount):
  self.balance=self.balance+amount
  return self.balance
# Method to withdraw money
 def withdraw(self,amount):
  if amount > self.balance:
    raise MyError("ERROR: Balance is less. No withdrawal.")
  else:
    self.balance=self.balance-amount
    return self.balance
# create bank objects
name=input("Enter the customer name: ")
acctype=input("Enter the account type (Type S for Saving or C for Current: ")
while acctype.upper() not in ["S","C"]:
  acctype=input("SorryInvalid entry.\nEnter the account type (Type S for Saving or C for Current: ")  
else:  
# The bank object is created with 0 balance
  b=bank(name,acctype)
while True:
   try:
     print("BANKING TRANSACTION\n")
     choice=input("Enter your choice. Type:\nd for  Deposit\nw for withdraw\ne for exit\n")
     if choice.lower()=="d":
       amt=float(input("Enter amount to deposit: "))
       print("Balance after deposit for customer ",b.custname," is : ",b.deposit(amt))
     elif choice.lower()=="w":
       amt=float(input("Enter amount to withdraw: "))
       print("Balance after withdraw for customer ",b.custname," is : ",b.withdraw(amt))
     elif choice.lower()=="e":
       break
     else:
       raise MyError("ERROR: Wrong choice!!") 
   except MyError as e:
       print(e)
       print()
   except(ValueError):
     print("Enter numeric value")    


'''You did a great job in implementing the exception class in the banking application.'''