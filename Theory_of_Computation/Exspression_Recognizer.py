import re

def REER(string):
    s = re.compile(r"""
    (-)?([\d]+\.[\d]+|[\d]+|(([\d]+\.[\d]+|[\d]+)?[a-z]))  # Expression must begin with a number, positive or negative
    (                                           
        [ ]*                                            # There can be whitespace between literals & operators
        (\+|-|\*|/|\^)                                  # All possible operators
        [ ]*                                            # There can be whitespace between literals & operators
    (-)?([\d]+\.[\d]+|[\d]+|(([\d]+\.[\d]+|[\d]+)?[a-z])) # Operators must have a number after them
    )+                                                  # There can be any number of additional expressions after
                                                        # the first one.
    """, re.VERBOSE)
    output = s.fullmatch(string)            # Additional Features: Exponent operator (^), variables with coefficients (3x, 2a, -2.6j), 
    return output

if __name__ == "__main__":
    input = input("Enter a mathmatical expression:")
    raw_input = r"{}".format(input)
    output = REER(raw_input)
    if output == None:
        print(input + " is NOT a valid mathmatical expression")
    else:
        print(input + " is a valid mathmatical expression")





