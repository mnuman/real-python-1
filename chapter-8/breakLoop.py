"""
Use a break statement to write a script that prompts the users for input repeatedly,
only ending when the user types “q” or “Q” to quit the program; a common way of
creating an infinite loop is to write while True
"""
while True:
    inputString = raw_input("Enter text,  or Q to stop: ")
    if inputString == "q" or inputString == "Q":
        break
    
