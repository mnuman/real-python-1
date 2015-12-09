"""
Write a script factors.py that includes a function to find all of the integers that divide
evenly into an integer provided by the user. A sample run of the program should look
like this (with the user’s input highlighted in bold):
1 >>>
2 Enter a positive integer: 12
3 1 is a divisor of 12
4 2 is a divisor of 12
5 3 is a divisor of 12
6 4 is a divisor of 12
7 6 is a divisor of 12
8 12 is a divisor of 12
"""
int_input = raw_input("Enter an integer number: ")
my_int = int(int_input)
for divisor in range(1,my_int+1):
    if my_int % divisor == 0:
        print "{} is a divisor of {} ".format(divisor, my_int)
