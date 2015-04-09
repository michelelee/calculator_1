# this one is like argv
def print_two(*args): 
    # "*" this astrik means to take all values and create a list 
    # there need to be a colon after defining a function or else it wont work 
    # in this case print_two is a function that is called at the bottom
    arg1, arg2 = args
    # in line one the print_two assigned the value for args and now arg1 is zedd 
    # and arg2 is shaw 
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    #in this line arg1 and arg2 are printed 

# ok that *args was pointless
def print_two_again(arg1, arg2):
    #zed is just trying to tell us that we can define parameters within the parens
    #after the function name in the first function above he defined it in line 6 
    #where as in this example he defined it within line 13
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    
    print "arg1: %r" % arg1

#this one takes no arguments
def print_none():
    print "I got nothin'"

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()








