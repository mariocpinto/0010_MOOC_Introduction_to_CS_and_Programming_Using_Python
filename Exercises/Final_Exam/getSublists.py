def getSublists(L, n):
    '''
    L: Non empty list of integers
    0 < n <= len(L)
    This function returns a list of all possible sublists in L of length n 
    without skipping elements in L. 
    The sublists in the returned list are ordered in the way they appear in L, 
    with those sublists starting from a smaller index being at the front of the list.
    '''
    
    subsets = []
    
    for start in range(len(L) - n + 1):
        subsets += [L[start:(start+n)]]
    
    return subsets

#L = [1, 1, 1, 1, 4]
#n = 2
#print getSublists(L, n)
#
#L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
#n = 4
#print getSublists(L, n)
    