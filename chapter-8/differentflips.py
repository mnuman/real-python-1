"""
Write a script coin_toss.py that uses coin toss simulations to determine the answer to this
slightly more complex probability puzzle:
I keep flipping a fair coin until I’ve seen it land on both heads and tails at least once each - in
other words, after I flip the coin the first time, I continue to flip it until I get a different result.
On average, how many times will I have to flip the coin total? Again, the actual probability
could be worked out, but the point here is to simulate the event using randint(). To get
the expected average number of tosses, you should set a variable trials = 10000 and a
variable flips = 0, then add 1 to your flips variable every time a coin toss is made. Then
you can print flips / trials at the end of the code to see what the average number of
flips was.
This one is tricky to structure correctly. Try writing out the logic before you start coding.
Some additional pointers if you’re stuck:
1. You will need to use a for loop over a range of trials.
2. For each trial, first you should check the outcome of the first flip.
3. Make sure you add the first flip to the total number of flips.
4. After the first toss, you’ll need another loop to keep flipping while you get the same
result as the first flip.
"""
from __future__ import division
from random import randint

def alternatesides():
    flip1 = randint(0,1)
    flips = 1
    while True:
        flips += 1
        # Stop whenever we flip different than the first flip
        if randint(0,1) != flip1:
            break
    return flips

totalflips = 0
NUM_FLIPS=1000000
for iteration in range(0,NUM_FLIPS):
    totalflips += alternatesides()

print "Alternate sides of the coin requires on average {} flips".format(totalflips/NUM_FLIPS)
