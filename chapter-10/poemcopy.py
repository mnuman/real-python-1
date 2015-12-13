"""
Write a text file output.txt that contains the same lines as poem.txt by opening both
files at the same time (in different modes) and copying the original file over line-byline;
do this using a loop and closing both files, then repeat this exercise using the
with keyword
"""
poem = open("poem.txt","r")
outp = open("output.txt","w")
r = poem.readline()
while r != "":
    outp.write(r)
    r = poem.readline()
poem.close()
outp.close()
