#Conditions along with Arithmetic operations


'''-----Task 1: Speed, Distance, Time Calculator------'''
print("****Task 1: ****")
print()
# Write a program which calculates the speed or distance or time depending on the inputs provided by the user
# Ask the user what they want to calculate and depending on the response, ask for the required inputs, 
# For example if the user says the speed needs to be calculated, take the distance and time as the input from the user
i=input("Select what you want to calculate:\n1.Speed    2.Distance  3.Time\n")
if i=="1":
  dist=float(input("Enter the distance: "))
  time=float(input("Enter the time: "))
  speed=dist/time
  print("The speed is: ",speed)
elif i=="2":
 speed=float(input("Enter the speed: "))
 time=float(input("Enter the time: "))
 dist=speed*time
 print("The distance is: ",dist)
elif i=="3":
  speed=float(input("Enter the speed: "))
  dist=float(input("Enter the distance: "))
  time=dist/speed
  print("The time is: ",time)
else:
  print("Incorrect selection. Select the correct number") 



'''-----Task 2: Total Score------'''
print("****Task 2: ****")
print()
# Write a program that takes the Maths theory and Maths lab score. 
# Each of the score cannot be more than 50 
# Calculate the total score and print the result
marks1=float(input("Enter your Maths theory marks:\n"))
marks2=float(input("Enter your Maths lab marks:\n"))
if marks1 > 50:
  print("Maths theory marks cannot be greater than 50")
elif marks2 > 50:
  print("Maths lab marks cannot be greater than 50")  
else:  
  total=marks1+marks2
  print("Total: ",total)

