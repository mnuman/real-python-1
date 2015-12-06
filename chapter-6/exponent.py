"""
Write a script exponent.py that receives two numbers from the user and displays
the result
of taking the first number to the power of the second number. A sample run of
the program
should look like this (with example input that has been provided by the user
                       included below):
"""
base = raw_input("Input base: ")
exponent = raw_input("Exponent: ")
print "{} to the power of {} = {}".format(base, exponent,
                                          float(base)**float(exponent))
