"""
Write a text file output.txt that contains the same lines as poem.txt by opening both
files at the same time (in different modes) and copying the original file over line-byline;
do this using a loop and closing both files, then repeat this exercise using the
with keyword
"""
with open("poem.txt","r") as poem, open("output.txt","w") as outp:
    for line in poem.readlines():
        outp.write(line)
        
