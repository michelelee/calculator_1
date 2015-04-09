
def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b
#here defined the fuction name as 'add', the function named add takes the input and prints "ADDING the the input"
#the only output is the string "adding a + b" the actual sum is not printed

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b
#here we do the same as the above function, the function named subtract takes the input and prints "SUBTRACTING the input"
#the ony output is the string

def multiply(a, b):
    print "MULTIPLYING %d + %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(30, 5) #we are assigning a value to the variable age by caling the fuction add with the parameters of 30 and 5 
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d , Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)
# printing a string that uses the variables above
# the variables get their value from when we called the functions in their assignment statement

# A puzzle for extra credit, type it anyway. 
print "Here is a puzzle."

what = add(age, subtract(height,multiply(weight, divide(iq, 2))))
# first we call the divide function with iq (above it becomes 50) and 2
# divide returns 25
# now the parameters for multiply are: (weight, 25) = weight is 180
# multiply returns 4500
# the next function subtract is called with the arguments: height (74) and 4500
# subtract returns -4436
# lastly, call add function to add age (35) and -4426
# add returns -4391





print "That becomes: ", what, "Can you do it by hand?"
