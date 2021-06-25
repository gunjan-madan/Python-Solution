#Chatbot
# Chatbot is a computer program that chats like a real person. For example Swelly is a Facebook Messenger chatbot.
# Take a look at this video, that shows what a conversational banking chatbot looks like:
# https://www.youtube.com/watch?v=SNQGypLBJys

'''Task 1: Product Inventory'''
print()
print("*** Task 1: ***")
print()
# You work in the inventory department of an Automobile company.
# You want to write a program that will help in:
# Taking the order quantity from the user and checking if there is enough stock of the item requested. [Hint: Set a value for the stock availability] 
# If there is then take the name, address and phone number from the user and let them know it will be sent to their address in 48 hrs.
# If not let the user know that, the item is not in stock and that they will receive an email once it is in stock
# Ensure that the user enters the name, phone and address
print("Hi! I am Invenie. I am here to take your order.")
name=input("Enter your name: ")
phone=input("Enter your phone number: ")
email=input("Enter your email address: ")
if name=="" or email=="" or phone=="":
 print("The name, email address and phone cannot be blank.")
else:
 item=int(input("Number of the autopart needed?: "))
 if item > 1000:
   print("Sorry item not in stock. You will receive an email once the item is in stock.")
 else:
   print("The items will be shipped within 48 hrs.")


'''------- Task 2: Flowers on a Click'''
print("*** Task 2: ****")
print()
# You have to write a program that asks a customer if they like bouquets 
# If yes, ask them to  select a flower bouquet of their choice. You can use the following to start with:
#  - Rose and Lily 
#  - Orchid and Tuberose
#  - Rose and Carnation 
#  - Carnation and Orchids 
# Once the customer specifies their choice, you need to:
#  - Tell them the cost
#  - Get their address
# And send a message that it will be delivered to that address and they can pay by card, cash or Google Pay
# If the customer does not like bouquets choice, tell them to visit the website
print("Hi!!Welcome to Flowers on a Click!")
print()
ans=int(input("Do you like flower bouquets? 1.Yes  2.No\n"))
if ans==1:
 choice=int(input("Which flower bouquet do you like(Select the number)?\nRose and Lily -1.Orchid and Tuberose 2.Rose and Carnation - 3.Carnation and Orchids : "))
 if choice==1:
  print("The cost for the bouquet is INR 250.")
  addr=input("Please enter the delivery address: ")
  print("Your bouquet will be delivered at :"+ addr + "\nYou can pay by card,cash or Googlepay")
 elif choice==2:
  print("The cost for the bouquet is INR 350.")
  addr=input("Please enter the delivery address: ")
  print("Your bouquet will be delivered at :"+ addr + "\nYou can pay by card,cash or Googlepay")
 elif choice==3:
  print("The cost for the bouquet is INR 300.")
  addr=input("Please enter the delivery address: ")
  print("Your bouquet will be delivered at :"+ addr + "\nYou can pay by card,cash or Googlepay")
 elif choice==4:
  print("The cost for the bouquet is INR 300.")
  addr=input("Please enter the delivery address: ")
  print("Your bouquet will be delivered at :"+ addr + "\nYou can pay by card,cash or Googlepay")
 else:
  print("Wrong choice try again.")
elif ans==2:
 print("Visit our website to get information about other services we provide.")
else:
 print("Wrong choice")