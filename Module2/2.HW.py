'''Task 1: Perimeter Calculator'''
print()
print("****Task 1: *****")
# Given below is a menu based Perimeter calculator.
# The calculator calculates the perimeter of:
# -  rectangle [Formula: 2*(length+width)]
# -  square [Formula: 4*length of side]
# -  circe[Formula: 2*(3.14*radius)]
# -  triangle [Formula: length + base + side]
# The menu has been created for you.
# Uncomment the statements and for each of the if statements write the relevant code.
#print("***** Perimeter Calculator *****")
#print("Select the shape for which the perimeter needs to be calculated")
#print("1. Rectangle")
#print("2. Square")
#print("3. Circle")
#print("4. Triangle")
#choice=int(input("Enter your choice: "))
#if choice==1:
  
#elif choice==2:
   
#elif choice==3:
   
#elif choice==4:
   
#else:
print("***** Perimeter Calculator *****")
print("Select the shape for which the perimeter needs to be calculated \n")
print("1. Rectangle")
print("2. Square")
print("3. Circle")
print("4. Triangle")
choice=input("Enter your choice: ")
if choice=="1":
 a=float(input("Enter the length: "))
 b=float(input("Enter the breadth: "))
 peri=2*(a+b)
 print("The perimeter of the rectangle is: ", peri)
elif choice=="2":
 a=float(input("Enter the length of the side: "))
 peri=4*a
 print("The perimeter of the square is: ",peri)
elif choice=="3":
 a=float(input("Enter the radius: "))
 peri=2*3.14*a
 print("The perimeter/circumference of the circle is: ",peri)
elif choice=="4":
 a=float(input("Enter the length of the first side: "))
 b=float(input("Enter the length of the second side: "))
 c=float(input("Enter the length of the third side: "))  
 peri=a+b+c
 print("The perimeter of the triangle is: ",peri)
else:
 print("You selection is wrong. Try again!!")