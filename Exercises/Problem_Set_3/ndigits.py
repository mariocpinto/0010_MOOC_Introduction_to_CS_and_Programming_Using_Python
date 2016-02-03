def ndigits(x):
    '''
    x: int
    returned value: number of digits in x
    '''
    # disregard sign of number
    x = abs(x)
    
    # If number is greater than single digit, divide by 10 
    #    and increase digit count by one, else return one.
    if x/10 != 0:
        return 1 + ndigits(x/10)
    else:
        return 1
