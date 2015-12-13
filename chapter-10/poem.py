poem = open("poem.txt", "r")
r = poem.readline()
while ( r != "" ):
    print r,
    r = poem.readline()
poem.close()    
