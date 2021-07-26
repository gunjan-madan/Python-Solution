''' Task 1: Nested Dictionaries '''
print("****** Task 1: ******")
print()
#Write a program to prepare a nested Dictionaries to store 3 sections of Grade 10 with 5 students in each section.
#Add StudentId, Name and Age in inner dictionary.


''' Task 1: Quiz Me '''
print("****** Task 1: *******")
print()
# The first event planned by Mr.Bumblebee is a quiz.
# Here are the list of questions:
# Question 1: Ants move in a line because of their sense of _________
# Ans: Smell
# Question 2: Poisonous teeth of the snakes are called as __________
# Ans.Fangs
# Question 3: The saltiest water body in the world is _______ sea
# Ans. Dead
# Question 4: An octagon has ___________ sides
# Ans. 8
# Question 5: Sum of the angles of any triangle is _______
# Ans. 180
# Write a program allowing players to:
# Select a number which corresponds to a question
# Take the answer as the input from the user and check if it is correct.
# Allow the user to continue playing, till he/she types “Exit”
print("\t\tQuiz")
quiz = {
 "question1" : "Ants move in a line because of their sense of _________",
 "answer1" : "smell",
 "question2" : "Poisonous teeth of the snakes are called as __________",
 "answer2" : "fangs",
 "question3" : "The saltiest water body in the world is _______ sea",
 "answer3" : "dead",
 "question4" : "An octagon has ___________ sides",
 "answer4" : "8",
 "question5" : "Sum of the angles of any triangle is _______",
 "answer5" : "180"}
exitch=""
while(exitch.lower()!="exit"):
 ch=input("Choose a number between 1 and 5: ")
 if ch=="1":
   print(quiz["question1"])
   ans=input("Answer: ")
   if ans.lower()==quiz["answer1"]:print("Correct Answer")
   else:print("Wrong Answer.Try Again!!")
 elif ch=="2":
   print(quiz["question2"])
   ans=input("Answer: ")
   if ans.lower()==quiz["answer2"]:print("Correct Answer")
   else:print("Wrong Answer.Try Again!!")
 elif ch=="3":
   print(quiz["question3"])
   ans=input("Answer: ")
   if ans.lower()==quiz["answer3"]:print("Correct Answer")
   else:print("Wrong Answer.Try Again!!")
 elif ch=="4":
   print(quiz["question4"])
   ans=input("Answer: ")
   if ans.lower()==quiz["answer4"]:print("Correct Answer")
   else:print("Wrong Answer.Try Again!!")
 elif ch=="5":
   print(quiz["question5"])
   ans=input("Answer: ")
   if ans.lower()==quiz["answer5"]:print("Correct Answer")
   else:print("Wrong Answer.Try Again!!")
 else:print("Please enter a number between 1 and 5")     
 exitch=input("Press Enter to continue or Exit to stop: ")
