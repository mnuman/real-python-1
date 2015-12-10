"""
1. Create a list named desserts that holds the two string values “ice cream” and “cookies”
2. Sort desserts in alphabetical order, then display the contents of the list
3. Display the index number of “ice cream” in the desserts list
4. Copy the contents of the desserts list into a new list object named food
5. Add the strings “broccoli” and “turnips” to the food list
6. Display the contents of both lists to make sure that “broccoli” and “turnips” haven’t
been added to desserts
7. Remove “cookies” from the food list
8. Display the first two items in the food list by specifying an index range
9. Create a list named breakfast that holds three strings, each with the value of “cookies”,
by splitting up the string “cookies, cookies, cookies”
10. Define a function that takes a list of numbers, [2, 4, 8, 16, 32, 64], as the argument
and then outputs only the numbers from the list that fall between 1 and 20
(inclusive)
"""
desserts = ['ice cream','cookies']
desserts.sort()
print "Index of ice cream is now: {}".format(desserts.index("ice cream"))
food = desserts[:]
food.append("broccoli")
food.append("turnips")
print "Desserts: " + str(desserts)
print "Food    : " + str(food)
food.remove("cookies")
print food[0:2]
breakfast = "cookies, cookies, cookies".split(", ")
print breakfast
