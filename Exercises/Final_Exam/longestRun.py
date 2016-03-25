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

def longestRun(L):
    '''
    L: Non empty list of integers
    This function returns the length of the longest run 
        of monotonically increasing numbers occurring in L. 
    '''
    for n in range(len(L),0,-1):
        subsets = getSublists(L, n)
        
        for subset in subsets:
            if sorted(subset) == subset:
                return n

#L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
#print longestRun(L)
#
#L = [7, 7, 2]
#print longestRun(L)
#
#L = [7, 2]
#print longestRun(L)
#
#L = [2]
#print longestRun(L)