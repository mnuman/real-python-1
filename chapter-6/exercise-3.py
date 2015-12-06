"""Write a function doubles() that takes one number as its input and doubles that number
three times using a loop, displaying each result on a separate line; test your function
by calling doubles(2) to display 4, 8, and 16"""
def doubles(x):
    for n in range(0,3):
        x *= 2
        print x
