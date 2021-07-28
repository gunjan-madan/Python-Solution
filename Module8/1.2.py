# A set is a collection which is unordered and unindexed. 
# Sets are written with curly brackets.

''' Task 1: Unique or Not '''
print("***** Task 1: *****")
print()
# In Python, you can use data structures called sets to perform operations like 
# - Combining items
# - Finding common items
# - Identifying unique items
# Uncomment the statements and click Run

#containerA = {"circle", "heart", "rectangle","cloud","star","bolt","moon","triangle","smiley"}
#print("Container A contains:\n",containerA )


print("***** Task 1: *****")
print()
# Create a similar set for containerB
containerB = {"circle","arrow","cloud","triangle","plus","flag"}
print(containerB)


''' Task 2:  Vowel Count ''' 
print("***** Task 2: *****")
print()
# Write a program to count number of vowels using sets in a given string
# The key steps to follow are:
# - Create a set of vowels  
# - Initialize a count variable to 0.
# - Using a for loop, check if the letter in the string is present in the set "vowel".
# - If it is present, the count variable is incremented.
def vowel_count(str):
# Initializing count variable to 0
 count = 0
 # Creating a set of vowels
 #vowel = set("aeiouAEIOU")
 vowel = ("a","e","i","o","u")
 # Loop to traverse the alphabet
 # in the given string
 for i in str:
 # Check if the alphabet is a vowel
   if i in vowel:
     count = count + 1
 print("No. of vowels :", count)
# Get the word from the user
str = input("Enter a word: ")
# Function Call
vowel_count(str.lower())

''' Task 3:  Languages Galore '''
print("***** Task 3: *****")
print()
# Uncomment the statements below and click Run

#lang={"Java","Python","C++","C#"}
## Add SQL to the set
#lang.add("SQL")
## Add HTML and Perl to the set
#lang.update(["HTML","Perl"])
##Number of items in the set
#print("The total number of items :",len(lang))
#print(lang)
##Remove C#
#lang.remove("C#")

# Here is the description to the methods used in the statements
# add() - Adds an item to a set
# update() - Adds multiple items to a set
# len() - Determines how many items a set has
# remove() - Removes an item from the set

# Uncomment the statements below and click Run

#lang1={"Java","Python","C++","C#","CSS"}
#lang2={"HTML","Perl","CSS"}
#print("Union: ",lang1 | lang2)
#print("Common: ",lang1 & lang2)
#print("Difference: ",lang1 - lang2)

# Here is the description of the operations used in the statements
# | means Union. It displays all items from both sets.
# & means Intersection. It displays items common to both sets
# - means Difference. The difference of the set lang1 from set lang2(lang1 - lang2) is a set of elements that are only in lang1 but not in lang2


''' Task 4: Dat(a)nalyst or Scientist '''
print("***** Task 5: *****")
print()
# Write a program detailing the skill set for a data scientist and data analyst.
# Create a set each for:
# - Data scientist - Python, R, SQL, Scala, Java, Hive
# - Data analyst -  Python, SQL, BI, Excel, Tableau, R
# Display the common skills between the two roles
# Display the skills unique to each role
# Add the following skills to each of the set:
# - Data scientist - Machine Learning, Hadoop
# - Data analyst - Statistics, NoSQL
Create the sets
datascientist = {"Python", "R", "SQL", "Scala", "Java", "Hive"}
datanalyst = {"Python", "SQL", "BI", "Excel", "Tableau", "R"}
print()
# Skill Set
print("Data Scientist Skills: ",datascientist)
print("Data Analyst Skills: ",datanalyst)
print()
# Common Skills
print("Common skills: ",datascientist & datanalyst)
print()
#Unique Skills
print()
print("Unique Data Scientist Skills: ",datascientist-datanalyst)
print("Unique Data Analyst Skills: ",datanalyst-datascientist)
# Add skills
datascientist.update(["Machine Learning", "Hadoop"])
datanalyst.update(["Statistics", "NoSQL"])
#Updated Skill Set
print()
print("Updated Data Scientist Skills: ",datascientist)
print("Updated Data Analyst Skills: ",datanalyst)
