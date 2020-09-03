import random

def randInt(min = 0, max = 100):
    if min > max:
        return "Not valid: Minimum number you have entered is greater than Max."
    elif max < 0:
        return "Max number is less that 0. Please enter a valid number"
    else:
        range = max - min
        num = int(random.random() * range + min) # min accounts for the min values when generating random num
        return f"Random number generator between {min} and {max}: {num} "
   

#print(randInt())                # should print a random integer between 0 to 100
# print(randInt(max=50)) 	    # should print a random integer between 0 to 50
# print(randInt(min=50)) 	    # should print a random integer between 50 to 100
# print(randInt(min=50, max=500))    # should print a random integer between 50 and 500

print(randInt())
print(randInt(max = 50))
print(randInt(min = 50))
print(randInt(min = 50, max = 500))
print(randInt(min = 500, max = 1000))
print(randInt(min= 500, max=100))





