"""Define a function, enrollment_stats(), that takes as an input a list of lists where each
individual list contains three elements: (a) the name of a university, (b) the total number of
enrolled students, and (c) the annual tuition fees.
Sample list:
1 universities = [
2 ['California Institute of Technology', 2175, 37704],
3 ['Harvard', 19627, 39849],
4 ['Massachusetts Institute of Technology', 10566, 40732],
5 ['Princeton', 7802, 37000],
6 ['Rice', 5879, 35551],
7 ['Stanford', 19535, 40569],
8 ['Yale', 11701, 40500]
9 ]
This function should return two lists: the first containing all of the student enrollment values
and the second containing all of the tuition fees.
Next, define a mean() and a median() function. Both functions should take a single list as
an argument and return the mean and median from the values in each list. Use the return
values from enrollment_stats() as arguments for each function. Challenge yourself by
finding a way to sum all the values in a list without using the built-in ‘sum()’ function for
calculating the mean.
At some point you should calculate the total students enrolled and the total tuition paid.
Finally, output all values:
1 *************************
2 Total students: 77285
3 Total tuition: $ 271905
4
5 Student mean: 11040
6 Student median: 10566
7
8 Tuition mean: $ 38843
9 Tuition median: $ 39849
10 *************************
"""
def mean(values):
    print values
    total = 0
    for i in values:
        total += int(i)
    return total/len(values)

def median(values):
    values.sort()
    num_els = len(values)
    if num_els %2 == 1:
        return values[num_els/2]
    else:
        return (values[num_els/2] + values[num_els/2-1])/2
    
def enrollment_stats(universities):
    students = []
    fees = []
    totalstudents = 0
    totaltuition = 0
    for uni in universities:
        students.append(uni[1])
        fees.append(uni[2])
        totalstudents += uni[1]
        totaltuition  += uni[2]
    print "Total students: {}".format(totalstudents)
    print "Total tuition: $ {}".format(totaltuition)
    print "Student mean: {}".format(mean(students))
    print "Student median: {}".format(median(students))
    print "Tuition mean: $ {}".format(mean(fees))
    print "Tuition median: $ {}".format(median(fees))


universities = [ ['California Institute of Technology', 2175, 37704],['Harvard', 19627, 39849],['Massachusetts Institute of Technology', 10566, 40732],['Princeton', 7802, 37000],['Rice', 5879, 35551],['Stanford', 19535, 40569],['Yale', 11701, 40500]]
enrollment_stats(universities)
