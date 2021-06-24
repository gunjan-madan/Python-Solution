#Practice on Nested Else if

''' Task 1: Metric Convertor'''
print("**** Task 1:  ****")
print()
# Write a Metric Conversion program that converts from one metric to another metric.
# You can start with:
# 1. cm to inch (Hint: divide the cm value by 2.54)
# 2. inch to feet (Hint: divide the inch value by 12)
# 3. meter to kilometer (Hint: divide the meter value by 1000)
# You can add more to the list.

print("Metric Convertor")
choice=input("Select your Option:\n1. cm to inch\n2. inch to feet\n3. meter to kilometer\n ")
if choice=="1":
 val=float(input("Enter the cm value: "))
 inch=val/2.54
 print("The value in inches: ",inch)
 ans=input("Do you want to convert from inch to cm: 1. yes 2.no: ")
 if ans=="1":
   val1=float(input("Enter the inch value: "))
   cm=val1*2.54
   print("The value in cm is: ",cm)
 elif ans=="2":
   print("Maybe next time")
 else:
   print("Wrong choice") 
elif choice=="2":
 val=float(input("Enter the inch value: "))
 inch=val/12
 print("The value in feet is: ",inch)
 ans=input("Do you want to convert from feet to inch: 1. yes 2.no: ")
 if ans=="1":
   val1=float(input("Enter the feet value: "))
   ft=val1*12
   print("The value in inches is: ",ft)
 elif ans=="2":
   print("Maybe next time")
 else:
   print("Wrong choice")     
elif choice=="3":   
 val=float(input("Enter the meter value: "))
 km=val/1000
 print("The value in km is: ",km)
 ans=input("Do you want to convert from km to meter: 1. yes 2.no: ")
 if ans=="1":
   val1=float(input("Enter the km value: "))
   m=val1*1000
   print("The value in meters is: ",m)
 elif ans=="2":
   print("Maybe next time")
 else:
   print("Wrong choice")
else:
 print("Wrong selection. Try again")   

