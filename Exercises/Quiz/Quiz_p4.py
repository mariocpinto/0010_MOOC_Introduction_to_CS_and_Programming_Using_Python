def isPalindrome(aString):
    '''
    (string) -> binary
    aString: a string
    
    Returned value: True if string is a palindrome, False otherwise
    '''
    # Your code here
    if aString == '':
        return True
           
    return (aString[0] == aString[-1]) and isPalindrome(aString[1:-1])
    
print(isPalindrome('ab'))