# Write the code for your lab 1 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab1.py
#
# Author: Lorenz Alvin Tubo
# Student Number: 109934224
#

def wins_rock_scissors_paper(player1,player2):
	#sets both input as lower case so its easier to check for conditional statements.
	player1 = player1.lower()             #1            runs once sets the enterd value to (lower player 1)
	player2 = player2.lower()             #1            runs once sets the enterd value to (lower player 2)

	if player1 == "rock" and player2 == "paper": #1       #first condition where player1 would lose
		return False                             #1 or 0      #exits none of the code below is called.
	
	if player1 == "paper" and player2 == "scissors": #1   #2nd condition where player1 would lose 
		return False								 #1 or 0  #exits none of the code below is implemented
	
	if player1 == "scissors" and player2 == "rock": #1    #3rd condition where player 1 would lose
		return False                                #1 or 0   #exits none of the code below is implemented

	if player1 == player2: #1         #4th condition in the instance of a draw.
		return False       #1 or 0         #exits none of the code below is called 

	return True #1 or 0                #if non of the conditions were triggered player1 won.

	#T = 1 + 1 + 1 + 1 + 1 + 1 + 1 
	#  = 7
    #  = O(1) constant time complexity

#this calculates a factorial of a given number, a factorial is a product of all number from 1 to the given number.
def factorial(a):
	ans = 1                  #1           #runs one initializing ans variable to 1 
	for i in range (1, a+1): #n       #iterates through all intigers from 1 to 'a' + 1 the given number.
		ans *= i             #n multiplies a to the current intiger in the loop
	return ans               #1       returns the end value of ans

	#T = 1 + n + n + 1 
	#  = 2n + 2
	#  = O(n) linear time complexity


def fibonacci(val):
	if val < 2:          #1     #runs once if the value of val is less than 2 
		return val   #1     #exits the function and returns the value of val without going 
			            #through the rest of the code 

	a,b = 0, 1 	      #1     #runs once if none of the guard clauses is triggered
	for _ in range (2, val + 1):      #n - 1  + 1      #runs n number of times + range()
		c = a + b     #n - 1   #runs n number of times depending on the size of the value.
		a, b = b, c   #n - 1     #runs everytime it loops 

	return b;             #1     #runs at the end of the function.

	#T = 1 + ((n - 1 )+ 1) + (n - 1) + (n - 1) + 1
	#  = 3n - 2 + 2
	#  = 3n
    #  = O(n) linear time complexity 


def sum_to_goal(num, goal):
    # 2 nested loops ensure that we don't check the same pair of numbers twice.
    for i in range(len(num)):              # n       # Outer loop iterates through the indices of the list
        for j in range(i + 1, len(num)):    # n - i + 2  # Inner loop iterates through the indices greater than the outer loop
            if num[i] + num[j] == goal:     # n       # Conditional statement that checks if the sum of the current pair of numbers equals the goal value
                return num[i] * num[j]      # 1       # If it passes the condition, returns the product of the two numbers and none of the code below is called.
    return 0                              # 1       # Returns 0 if no pair of numbers sums to the goal value

# T = n * (n - i) + 2 + n + 1     #only 1 because only one of the returns can be called.
#   = n^2 - ni + 3    
#   = O(n^2) Quadratic time complexity

class UpCounter:
	def __init__(self, step_size = 1):
		self.count_value = 0 #1                   value of the range of count depending if u wanna count to 10 or etc.. 
		self.step_size = step_size #1             controls the range of movement either 1 up or 2 up.

	def count(self):
		return self.count_value #1                returns the size of count.

	def update(self):
		self.count_value += self.step_size #1     moves up depending on the set value of step_size


class DownCounter(UpCounter): #                   inheriting from the UpCounter class
	def update(self): #                           overloads the update function of UpCounter Class
		self.count_value -= self.step_size #1     instead of incrementing it decrements.


#T = 1 + 1 + 1 + 1 + 1
#  = 5
#  = O(1)  Constant time complexity
