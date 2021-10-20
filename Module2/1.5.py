# Do you know what the Pythagoras Theorem is? 
# The Pythagoras theorem states that “In a right-angled triangle,  the square of the hypotenuse side is equal to the sum of squares of the other two sides“. 
# The sides of this triangle have been named as Perpendicular, Base and Hypotenuse.
# The hypotenuse is the longest side, as it is opposite to the angle 90°.

"""-------Task 1:  What's missing in the right angled triangle? ------"""
print(" ")
print("*** Task 1: ***")

# Write a program to calculate the hypotenuse or one of the sides of the right angled triangle.
chk = input('Has the length of the hypotenuse been given?(yes or no) ')
if chk == 'no' or chk == 'n':
  a = float(input('enter the length of one of the sides:'))
  b = float(input('enter the length of the other side: '))
  c = float((a**2 + b**2)**.5)
  print ('hypotenuse:', c)  
elif chk == 'yes' or chk == 'y':
  c = float(input('enter the length of the hypotenuse: '))
  b = float(input('enter the length of the known side: '))
  if b > c:
      print ('The side cannot be longer than the hypotenuse, try again.')
  else:
      a = (c**2 - b**2)**.5
      print ('Length of the side is:', a)
else:
  print ('You must enter either "yes" or "no"')



''' Awesome!! You have successfully created a Pythagorean Theorem calculator. Congratulations!!'''