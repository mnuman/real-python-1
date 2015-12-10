"""10. Define a function that takes a list of numbers, [2, 4, 8, 16, 32, 64], as the argument
and then outputs only the numbers from the list that fall between 1 and 20
(inclusive
"""
def lister(mylist):
    for i in mylist:
        if i >= 1 and i <= 20:
            print i

lister([1,2,5,90,45,12])
