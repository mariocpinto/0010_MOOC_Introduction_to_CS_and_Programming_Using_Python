def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    value = 0
    
    for i in range(0,len(listA)):
        value += listA[i]*listB[i]
    
    return value
    