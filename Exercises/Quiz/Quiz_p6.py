def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    new_list = []
    
    for element in aList:
        if type(element) != list:
            new_list += [element]
        else:
            new_list += flatten(element)
    
    return new_list
    
# print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))
# Expected o/p: [1,'a','cat',2,3,'dog',4,5]

# print(flatten([[1,'a',['cat', ['a','pi']],2],[[[3]],'dog'],4,5]))
# Expected o/p: [1, 'a', 'cat', 'a', 'pi', 2, 3, 'dog', 4, 5]
