# Modify this function to return a list of strings as defined above
def list_benefits():
    return ("More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together")

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    # receives a single argument containing a string 
    # returns a sentence starting with the given string 
    # ends with the string " is a benefit of functions!"
    new_string_from_benefit = benefit + " is a benefit of functions!"
    return new_string_from_benefit


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    # now list_of_benfits = 4 items: ("More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together")
    for benefit in list_of_benefits:
        print build_sentence(benefit)
        

name_the_benefits_of_functions()



 