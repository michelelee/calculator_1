def cheese_and_crackers(cheese_count, boxes_of_crackers): 
    # we defined a function that takes two variables
    print "You have %d cheeses!" % cheese_count 
    #function prints, completes the sentence with the amount of cheese we have
    # cheese_count will be defined when we call the function
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket. \n" # the \n tells the program to start a new line after this statement
#this is the end of the first function

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)
# we called the function and defined the parameters!!

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
# we are assigning values to two new variables

cheese_and_crackers(amount_of_cheese, amount_of_crackers) 
# this time we call the function using variable names as the parameters/arguments. the variables are assigned above.
# this is the 2nd time we run the function in this program. Its a separate and new time!

print "We can even do math inside too."
cheese_and_crackers(10 + 20, 5 + 6 )
# we called the function again, this time using mathy expressions for the arguments

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
# we called the function again. this time the parameters are variables and math expressions combined
# we added to our existing variables when we put them in as parameters
