# Have you wondered if there is a way by which we can decide the format of how a string is displayed? [Wait for the student to respond]
# For example, aligning the text displayed or setting decimal values.
# Let's take a look on how Python can help us. 

'''Task 1: Setting the Placeholder'''
print("***** Task 1: *****")
print()
# Uncomment the below statements and click Run. Observe the output.
txt1 = "Hi I am {name}, and am {age} years old".format(name = "Ria", age = 12)
print(txt1)
# What exactly happened?
# The format() method inserted the name and age in the text where the{ } braces were placed. The { } are called placeholders. 
# Here are some more examples. Uncomment the statements and click run. Observe the output.
txt2 = "Hi I am {0}, and am {1} years old".format("Ria",12)
print(txt2)
txt3 = "Hi I am {}, and am {} years old".format("Ria",12)
print(txt3)
#Without decimal places
txt = "For only {price} dollars!"
print(txt.format(price = 25))
#With two-decimal format (include 2 decimal points)
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 25))
#Use "-" to specify if the number is negative.Positive numbers are displayed without any sign):
txt = "The temperature today is {:-} degrees celsius."
print(txt.format(-2))
# In the above statements you would have noticed the following functionalities:
# {0}, {1} - Denotes the position of the string or in other words are the numbered placeholder
# {} - Denotes empty placeholders where the value will be  be substituted
# {price:.2f} - 2f is used to include 2 decimal places when displaying the value stored in the variable price
# {:-} - “-”  is used to specify that the number is negative

'''Task 2: Fill the missing gaps'''
print("***** Task 2: *****")
print()
# Given below is a story that has placeholders, wherein you need to fill values using the format method.
# Lets see the story that you come out with.
# Uncomment the statements below, fill in the values for the format method and see how the story unfolds.
txt1 = "Kabir is {} years old and studied in {} grade in his hometown {}".format("11",5,"Mysore")
txt2 = "One of Kabir's hobbies is {} and he spends {} hours everyday trying to master it".format("painting",2)
txt3 = "He wishes to become {} once he grows up and serve the {}".format("doctor","nation")
print(txt1)
print(txt2)
print(txt3)


'''Task 3 : Role Model'''
print("***** Task 3: *****")
print()
# Write a program in which you use the format() method to describe your favourite role model
txt1 = "Sudha Murthy is an {} who writes stories in {} and {}.".format("author","english","kannada")
txt2 = "I love her stories because of the {} she portrays.".format("simplicity")
txt3 = "I have ready about {} books of hers and my all time favourite is {}.".format(8,"House of Cards")
print(txt1)
print(txt2)
print(txt3)



'''Fantastic!! You have become confident in working with in-built functions. Awesome!!'''