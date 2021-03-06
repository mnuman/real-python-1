﻿"""
Write a script election.py that will simulate an election between two candidates, A and B.
One of the candidates wins the overall election by a majority based on the outcomes of three
regional elections. (In other words, a candidate wins the overall election by winning at least
two regional elections.) Candidate A has the following odds:
• 87% chance of winning region 1
• 65% chance of winning region 2
• 17% chance of winning region 3
Import and use the random() function from the random module to simulate events based on
probabilities; this function doesn’t take any arguments (meaning you don’t pass it any input
variables) and returns a random value somewhere between 0 and 1.
Simulate 10,000 such elections, then (based on the average results) display the probability
that Candidate A will win and the probability that Candidate B will win.
Hint: To do this, you’ll probably need to use a for loop with a lot of if/else statements to
check the results of each regional election.
"""
from __future__ import division
from random import random

AWins = 0
BWins = 0
for n in range (0,10000):
    if (random() < 0.87) + (random() < 0.65) + (random() < 0.17) >= 2:
        AWins +=1
    else:
        BWins +=1

print "A wins {}, B wins {} out of {} elections. Change that A wins is: {}".format(AWins, BWins, AWins + BWins, AWins / (AWins + BWins))
