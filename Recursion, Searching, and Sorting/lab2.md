# Lab 2


### function 1:

Analyze the following function with respect to number

```python
def function1(number):
	total=0; #1              initializes the variable total to zero

	for i in range(0,number):    #n + 1 runs n number of time + 1 for range()
		x = (i+1)                #n   runs n number of times. 
		total+=(x*x)             # n + 2   runs n number of times and 2 as there are 2 operations

	return total                 #1      returns the value of total.

#T = 1 + (n + 1) + (n + 2) + n + 1
#  = 3n + 5 
#  = O(n) linear time complexity
```

### function 2:

Analyze the following function with respect to number

```python
def function2(number):#takes in the parameter number.
	return  ((number)*(number+1)*(2*number + 1))/6  #1 

# T = 1
#   = 1
#   = O(1) constant time complexity

```

### function 3:

Analyze the following with respect to the length of the list.  Note that the function call len() which returns the length of the list is constant (O(1)) with respect to the length of the list.
```python

def function3(list):
    # Outer loop iterates from 0 to len(list) - 1, O(n)
    for i in range(0, len(list) - 1):
        # Inner loop iterates from 0 to len(list) - 1 - i, O(n)
        for j in range(0, len(list) - 1 - i):
            # Conditional compares elements in the list, O(1)
            if list[j] > list[j + 1]:
                # Temporary variable used for swapping values, O(1)
                tmp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = tmp

# T = n * n * 1 * 1 * 1
#   = O(n^2) Quadratic time complexity
```
### function 4:

Analyze the following function with respect to number

```python
def function4(number): #accepts parameter number 
	total=1#1            initializes variable total value to 1 
	for i in range(1 to number):# n - 1 + 1  #since it starts from 1 and not 0 (-1) because of range() it goes to +1 
		total=total*(i+1)#n - 1   #alters the value of total
	return total #1               #outputs the total

#T = 1 + ((n - 1) + 1) + (n - 1) + 1
#  = 2n - 2 + 3 
#  = 2n + 1 
#  = O(n) linear time complexity 
```


## In class portion


### Group members
List the members of your group member below:

	* Name 
	* Lorenz Alvin Tubo
	* Fausto Javier Zaruma

### Timing Data
Note, if a groupmate did not complete lab1, simply put 0.0 in for the times, it is ok if there is something missing.

| Team member | Timing for fibonacci | Timing for sum_to_number | 
|---|---|---|
| Lorenz Alvin Tubo |  0.0000519 | 0.816 |
| Fausto Zaruma     |  0.000320 | 0.560  |
| group member 3 | 0.0 | 0.0 |
| group member 4 | 0.0 | 0.0 |
| group member 5 | 0.0 | 0.0 |
| group member 6 | 0.0 | 0.0 |

### Summary 

| function | fastest | slowest | difference
|---|---|---|---|
|sum_to_number | 0.560 | 0.816 | 0.256 |
|fibonacci | 0.0000519 | 0.000320 | 0.000199 |


### Discussion:

Over all our approaches where quite similar except for variable naming approaches and condition styling in the looping parts, nonetheless, both implementations used a nested for loop for the sum_to_goal function. Upon further runs we observed a substantial difference in the time performance indicators leading to Lorenz having a faster performance than Fausto's output, these is most likely related to hardware features for both participants. In conclusion, the computer system and hardware characteristic of the device play a huge role in determining their efficiency, as you can observe in the sum_to_goal algorithms comparison. As per the Fibonacci function, Fausto's implementation, ran in a relatively fast device, was still short compared to Lorenzo's. The main reason behind this is that Fausto is constantly storing all the results of the sequence when the function does not require more than a single number of it, leading to a slower code, regardless of the hardware advantages.

## Reflection

1. Considering the solutions you saw when looking at the lab 1 code, what differences did you see between fastest and slowest versions of code?
For the fibonacci function Fausto's implementation was slower compared to mine. Considering  mine uses an iterative method and it avoids redundant calculations by only keeping track of the current and previous fibonacci numbers. While my groupmates fibonacci uses a list(results) to store Fibonacci numbers. It checks if the requested fibonacci number is already available in the list before calculating futher. These added constraints make my code faster than Faustos only for smaller values but would make his relatively faster for larger values. In the sum_to_goal function both our code uses nested loops, resulting in quadratic time complexity for finding pairs to a goal value. therefore there is no significant difference in runtime efficiency between them.
2. Was there a difference in terms of usage of space resource?  Did one algorithm use more/less space (memory)? 
 In the space usage for sum_to_goal both our functions did not create any additional data structures that grow in the input size. But in terms of the fibonacci fucntion faustos code uses a list to store the fibonacci numbers the size of the list grows proportionally with the input value. But my Fibonacci uses a constant amount of memory to store a few variables these variables are updated with each iteration of the loop and the size of the variables does not depend on the input. 
3. What sort of conclusions can you draw based on your observations?
In conclusion, my fibonacci function is more efficient that my group mates method since it doesnt create a data structure and would run faster. Both our sum_to_goal functions have the same time complexity. My space complexity for the fibonacci sequence is more efficient than my groupmates space complexity for the same function. Computer systems and hardware characteristics also play a huge role on time efficiency.



