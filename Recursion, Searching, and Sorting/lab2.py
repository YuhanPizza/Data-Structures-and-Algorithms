# copy over your code from lab 1 to this file

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
        for j in range(i + 1, len(num)):    # (n - 1, 2 ,3 .... )+ 2  # Inner loop iterates through the indices greater than the outer loop
            if num[i] + num[j] == goal:     # n       # Conditional statement that checks if the sum of the current pair of numbers equals the goal value
                return num[i] * num[j]      # 1       # If it passes the condition, returns the product of the two numbers and none of the code below is called.
    return 0                              # 1       # Returns 0 if no pair of numbers sums to the goal value

# T = n * n * 1 * 1 + 1 #only 1 because only one of the returns can be called.
#   = O(n^2) Quadratic time complexity

    