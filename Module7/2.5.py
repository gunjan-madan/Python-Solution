''' Task 1: Three Dice '''
print("****** Task 1: ******")
print()
# The next game that Mr.Bumblebee has planned is called "Three Dice". 
# The rules of the game is as follows:
# - Each dice has three sides each.
# - Each of  side of the dice has the number 1, 2 and 3 printed
# - A player rolls  all the three dice. On rolling
# - If he gets all three of the same number, the program displays "Rollzee"
# - If he gets two of the same number, the program display "Two of a kind"
# - If he gets one of each number, the program displays "One of a kind".
# The player gets to roll the dice as long as he wants.
# If he wants to quit the game, he needs to type "Exit"

import random
exitch=""
dice={"val1":0,"val2":0,"val3":0}
while exitch.lower()!="exit":
   print("Dice has been rolled")
   for i in dice:  # "Roll" the dice to get a random number between 1-3
    dice[i] = random.randint(1,3)
   if dice["val1"]==dice["val2"]==dice["val3"]:
     print(dice.values())
     print("Rollzee")
   elif dice["val1"]==dice["val2"] or dice["val1"]==dice["val3"] or dice["val2"]==dice["val3"]:
     print(dice.values())
     print("Two of a kind")
   else:
     print(dice.values())
     print("One of a kind")
   exitch =input("Press enter to keep playing or type exit to stop playing: ")

''' Task 2: What's the capital? '''
print("****** Task 2: ******")
print()
# The final game of the community event is “Guess the Capital”.
# You have created a similar program in your earlier “if-else” lesson. 
# You can either change that program or use the list below to create a new program.
# Here is the list of the country and its capitals:
# India - New Delhi
# Afghanistan - Kabul
# Brazil - Brasilia
# Canada - Ottawa
# Indonesia - Jakarta
# Ireland - Dublin
# Netherlands - Amsterdam
# Norway - Oslo
# Turkey - Ankara
# Vietnam - Hanoi
# Mr.Bumblebee want you to create a game where :
# - A player has to guess the capital of the country
# - For each correct answer, the player gets one point
# - At the end of the game, the total score needs to be displayed
print("-----Guess the Capital-----")
countcap={"India":"New Delhi",
          "Afghanistan":"Kabul",
          "Brazil":"Brasilia",
          "Canada":"Ottawa",
          "Indonesia":"Jakarta",
          "Ireland":"Dublin",
          "Netherlands":"Amsterdam",
          "Norway":"Oslo",
          "Turkey":"Ankara",
          "Vietnam":"Hanoi"}
cnt=0
for i in countcap:
 print("What is the capital of ",i)
 ans=input()
 if ans.lower()==countcap[i].lower():
    print("Correct")
    cnt=cnt+1
 else:
    print("Incorrect")
print("Your score is: ",cnt," out of 10")

