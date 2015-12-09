""" Write a script that simulates 10,000 throws of dice and displays the average number
resulting from these tosses"""

from __future__ import division
from random import randint

def die():
    return randint(1,6)

sumdie = 0
for i in range(0,100000):
    sumdie += die()

print "Average: {}".format(sumdie/100000.0)
    
