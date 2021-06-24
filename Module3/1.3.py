
# In one of the previous lessons, you used the print statement to create text art.
# Imagine using the while loop command and the print statements to generate some really awesome text art.
# Let's help Sam create some great text art. All set to give it a try!

'''Task 1: Pattern Printing'''
print("**** Task 1: ****")
print()
# Uncomment the statements below and click Run to see what is displayed
print("**pattern1**")
i=1
while(i<=5):
 print("*"*i)
 i=i+1
# Wow!! Wasn't that awesome!! Now if you want to reverse the pattern, how will you change the code to generate it?
print()
print("--Pattern 2--")
print()
i=5
while(i>=1):
 print("*"*i)
 i=i-1   


'''Task 2: Combination Pattern'''
print("**** Task 2: ****")
print()
# Ready for the next challenge!
# You just created two patterns. Try combining them and see what you get
print("**Pattern 3**")
i=1
while(i<=5):
 print("*"*i)
 i=i+1
while(i>=1):
 print("*"*i)
 i=i-1




'''Task 3: Dazzling Diamond'''
print("**** Task 3: ****")
print()
# Given below is the code that will create a diamond text art on your terminal output window.
# A part of the program has been done for you.
# You need to uncomment the code below and fill in the missing details in while statement and the counters (i and d)
# Once you are done, click Run and see the diamond unfold.
print("**Diamond Pattern**")
print()
i=5 # First half of the diamond
d=1
while(i>=1):
 print("*"*i+" "*d+"*"*i)
 i=i-1
 d=d+2
i=1 #Second Half of the diamond
d=9
while(i<=5):
 print("*"*i+" "*d+"*"*i)
 i=i+1
 d=d-2




'''Fantastic!! You have created some great art work!! You definitely have a wonderful creative side.'''


