# Lets create ATM Machine program/


''' Task 1:  Attributes and Functions of Bank Class '''
print("***** Task 1: *****")
print()
# Identify the attributes and functions of a Bank Class
# Graphically represent the same on a paper



''' Task 2:   Banking in Action '''
print("***** Task 2: *****")
print()
# Using the class design you have specified in Task 1 create the: 
# - bank class 
# - attributes and methods of the bank class

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
     print("Balance is less. No withdrawal.")
   else:
     self.balance=self.balance-amount
     return self.balance
 
# create bank objects
name=input("Enter the customer name: ") 
acctype=input("Enter the account type (Type S for Saving or C for Current: ")
# The bank object is created with 0 balance
b=bank(name,acctype)
 
while True:
 print("BANKING TRANSACTION\n")
 choice=input("Enter your choice. Type:\nd for Deposit\nw for withdrawal\ne for exit\n")
 if choice.lower()=="d":
   amt=float(input("Enter amount to deposit: "))
   print("Balance after deposit for customer ",b.custname," is : ",b.deposit(amt))
 elif choice.lower()=="w":
   amt=float(input("Enter amount to withdraw: "))
   print("Balance after withdrawal for customer ",b.custname," is : ",b.withdraw(amt))
 elif choice.lower()=="e":
   break
 else:
   print("Wrong choice!")   
