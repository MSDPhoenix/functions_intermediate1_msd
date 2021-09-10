# the goal of this assignment is to 
# write a single function, randInt() 
# that takes up to 2 arguments.

# If no arguments are provided, the function should return a random integer between 0 and 100.

# If only a max number is provided, the function should return a random integer between 0 and the max number.

# If only a min number is provided, the function should return a random integer between the min number and 100

# If both a min and max number are provided, the function should return a random integer between those 2 values.

import random
def randInt(min=0,max=100):
    if max<0:
        return("I don't know what you want me to do.")
    elif min>max:
        min,max=max,min
        num = round(min+(random.random()*(max-min)))
        return num
    else:
        num = round(min+(random.random()*(max-min)))
        return num




#print(randInt()) 		            # should print a random integer between 0 to 100
#print(randInt(max=50))             # should print a random integer between 0 to 50
#print(randInt(min=50))              # should print a random integer between 50 to 100
#print(randInt(min=50, max=500))     # should print a random integer between 50 and 500
#print(randInt(min=500, max=50))     # should print a random integer between 50 and 500
print(randInt(max=-3)) 		         # should print a random integer between 0 to 100