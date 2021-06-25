# Have you wondered what would happen if you had an infinite loop? 
# It is important to break away from an infinite loop else, the computer keep processing without any end
# Let us take a look at some programs that help break from a loop

'''Task 1: Whats the price '''
print("**** Task 1: ****")
print()
# Write a program that takes the price of goods sold as inputs from the user.
# To stop entering or when the user is done, he or she news to press 0.
# Once the user is done,the program must print
# - Total cost  of the goods 
# - Total number of goods.
inp=1
ctr=0
sumt=0
print("Input the price of the goods.\nPress 0, when you want to stop")
print()
while(inp!=0):
 inp=float(input("enter the price: "))
 sumt=sumt+inp
 ctr=ctr+1
print("The total number of goods sold: ",ctr-1)
print("The total price is: ",sumt)





'''Task 2: Lemonade and Glasses '''
print("**** Task 2: ****")
print()
# Your friend Sam has a jar with 5 cups of fresh lemonade.  
# Jack has some glasses which hold 1.5 cups each of liquid.  
# How many glasses of lemonade can Jack serve?
jar = 5
glass_amount = 1.5
served_glasses = 0
while jar > 0:
   jar = jar - glass_amount
   served_glasses = served_glasses + 1
print("The number of glasses served are: ", served_glasses)



'''Task 3: Population Calculator '''
print("**** Task 3: ****")
print()
# Sam is thrilled how he is able to solve problems
# He now wants to solve a population projection problem
# Can you solve it for him?
# He wants to know how long will it take to reach a certain target population (in years), given a 
# - starting population =10000000
# - birthrate=0.015
# - deathrate=0.023
# - Reduction can be taken as 0.1.
# Hint1: Target population can be calculated as population * reduction
# Hint2: Change in population can be calculated using the formula (current_pop * birthrate) - (current_pop * deathrate)
population = 10000000.0
birthrate = 0.015
deathrate = 0.023
reduction = 0.1
current_pop = population
target_pop = population * reduction
years = 0
change_pop = 0.0
while (current_pop >= target_pop) :
   change_pop = (current_pop * birthrate) - (current_pop * deathrate)
   current_pop = current_pop + change_pop
   years = years + 1
print("Number of years until target population reached: ", years)


'''Great! You are exceptionally good at coming out with programming solutions. Way to go!!'''