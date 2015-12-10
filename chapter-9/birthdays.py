"""
Create an empty dictionary named birthdays
2. Enter the following data into the dictionary:
1 'Luke Skywalker': '5/24/19'
2 'Obi-Wan Kenobi': '3/11/57'
3 'Darth Vader': '4/1/41'
106
3. Write if statements that test to check if ‘Yoda’ and ‘Darth Vader’ exist as keys in the
dictionary, then enter each of them with birthday value ‘unknown’ if their name does
not exist as a key
4. Display all the key-value pairs in the dictionary, one per line with a space between the
name and the birthday, by looping over the dictionary’s keys
5. Delete ‘Darth Vader’ from the dictionary
6. Bonus: Make the same dictionary by using dict() and passing in the initial values
when you first create the dictionary
"""
birthdays = {'Luke Skywalker': '5/24/19','Obi-Wan Kenobi': '3/11/57','Darth Vader': '4/1/41'}
if "Darth Vader" not in birthdays:
    birthdays["Darth Vader"] = "1/1/02"
if "Yoda" not in birthdays:
    birthdays["Yoda"] = "1/2/03"

for b in birthdays:
    print b, ":", birthdays[b]
    print ""
del(birthdays["Darth Vader"])    
    
