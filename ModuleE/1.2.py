#Implicit exceptions
''' Task 1:  Exception(al) '''
print("***** Task 1: *****")
print()
# Uncomment each block of code, one at a time, and analyze the output

##TypeError
# x="10"
# y=2
# a=x/y

##NameError
#b=p/2

##ZeroDivisionError
# c=10/0

# try:
#   num1=int(input("Enter first number: "))
#   num2=int(input("Enter second number: "))
#   result= num1/num2
# except ValueError:
#   print("Make sure numeric values are provided for both numbers")
# except ZeroDivisionError:
#   print("Division by zero")
# else:
#   print("The result is ",result)

''' Task 2:  Try and Succeed '''
print("***** Task 2: *****")
print()
#Handle the exception in following program
#Hint: First run and observe the error occured

# def myPython(msg):
#   return message

# mypython("Hello")

''' Task 3:  Try and Succeed '''
print("***** Task 3: *****")
print()
#Handle the exception in following program
#Hint: First run and observe the error occured


# randomList = [a, 0, 2, "&"]

# i=0
# while i <= 4:
#   entry=randomList[i]
#   print("The entry is", entry)
#   r = 1/int(entry)
#   print("The reciprocal of", entry, "is", r)
#   i=i+1

try:
  a=1
  randomList = [a, 1, 2, "&"]

  i=0
  while i <= 4:
    entry=randomList[i]
    print("The entry is", entry)
    r = 1/int(entry)
    print("The reciprocal of", entry, "is", r)
    i=i+1
except NameError:
  print("Please define all variables")
except ValueError:
  print("Please make all the values in the list are numbers")
except ZeroDivisionError:
  print("Please do not divide by 0")


''' Task 4: Multiple Exceptions '''
print("***** Task 3: *****")
print()
#Handle all above mentioned exceptions in once except block
try:
  a=1
  randomList = [a, 1, 2, "&"]

  i=0
  while i <= 4:
    entry=randomList[i]
    print("The entry is", entry)
    r = 1/int(entry)
    print("The reciprocal of", entry, "is", r)
    i=i+1
except (NameError, ValueError, ZeroDivisionError):
  print("Please define all variables")
