"""Write a script that prompts the user to enter a word using the raw_input() function,
stores that input in a string object, and then displays whether the length of that string
is less than 5 characters, greater than 5 characters, or equal to 5 characters by using a
set of if, elif and else statements
"""
my_string = raw_input("Gimme some string: ")
if len(my_string) < 5:
    print "Your string is less than 5 characters"
elif len(my_string) == 5:
    print "Your string is exactly 5 characters"
else:
    print "Your string is longer than 5 characters"    
