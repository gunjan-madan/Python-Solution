# In the previous lesson, you used if-elif-else statements to create a menu based program.
# Now let us take a look at using nested if-elif statements in creating menu based programs.
'''Task 1: Nested If-else'''
print()
print("*** Task 1: ***")
print()
#Make a variable like winning_number and assign any number to it between 1 and 20.
#Ask user to guess a number between 1 and 20. (Take input)
#if user guessed correctly, print "YOU WIN"
#if user didn't guessed correctly then:
  #if user guessed lower than actual number, then print "TOO LOW"
   #if user guessed lower than actual number, then print "TOO HIGH"

winning_number=15
user_input=int(input("Guess a number between 1 and 20: "))
if user_input== winning_number:
  print("YOU WIN!!")
else:
  if user_input<winning_number:
    print("TOO LOW")
  else:
    print("TOO HIGH")

'''Task 2: Nested If-else'''
print()
print("*** Task 2: ***")
print()
#This is a program to tell User the shipping cost based on the country and the weight.
#Write a Program that takes two inputs: country_code(AU/US) and weight of the product.
#Use the following conditions to find the shipping cost
#country          Product Size               Shippping cost
#US               less than 1kg               $5
#US               between 1 and 2kg           $10
#US               greater than 2kg            $20
#AU               less than 1kg               $10
#AU               between 1 and 2kg           $15
#AU               greater than 2kg            $25

print("This Program will caluculate Shipping Cost")
country_code=input("Enter the country code. Press 1 for 'US'. Press 2 for 'AU':")
weight=float(input("Enter the weight of the Product(in kgs): "))

if country_code=="1":
  if weight<1.0:
    print("Shipping Cost is  $5")
  elif weight<2.0:
    print("Shipping Cost is  $10")
  else:
    print("Shipping Cost is  $20")
elif country_code=="2":
  if weight<1.0:
    print("Shipping Cost is  $10")
  elif weight<2.0:
    print("Shipping Cost is  $15")
  else:
    print("Shipping Cost is  $25")
else:
  print("Please provide a valid input.")