"""Write a script invest.py that will track the growing amount of an investment over time. This
script includes an invest() function that takes three inputs: the initial investment amount,
the annual compounding rate, and the total number of years to invest
"""
def invest(amount, rate, time):
    """Calculate the value of the investment of amount using a interest rate
for time in years.
    Example:
    principal amount: $100
    annual rate of return: 0.05
    year 1: $105.0
    year 2: $110.25
    year 3: $115.7625
    year 4: $121.550625
    year 5: $127.62815625
    year 6: $134.009564063
    year 7: $140.710042266
    year 8: $147.745544379
"""
    print "principal amount: $", amount
    print "annual rate of return: ", rate

    for n in range(0, time):
        amount *= 1+rate
        print "year {}: ${}".format(n+1, amount)
        
    
