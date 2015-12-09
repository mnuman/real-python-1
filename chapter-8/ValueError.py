""" Write a script that repeatedly asks the user to input an integer, displaying a message
to “try again” by catching the ValueError that is raised if the user did not enter an
integer; once the user enters an integer, the program should display the number back
to the user and end without crashing
"""
while True:
    try:
        i = raw_input("Enter number: ")
        n = int(i)
        print "You entered the number: " + str(n)
        break
    except ValueError:
        print "Try again,brother !" 
