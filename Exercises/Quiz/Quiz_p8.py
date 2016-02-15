def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Create a copy of the original list
    L_cp = L[:]
    
    for item in L_cp:
        if not f(item):
            L.remove(item)
    
    return len(L)
    
run_satisfiesF(L, satisfiesF)

#def f(s):
#    return 'a' in s
#      
#L = ['a', 'b', 'a']
#print satisfiesF(L)
#print L

# Expected output:
#2
#['a', 'a']