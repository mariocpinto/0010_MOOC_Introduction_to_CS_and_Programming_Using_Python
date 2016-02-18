def Hash(wordList, alphabet, hashFunction):
    '''
    wordList: List of words to be hashed
    alphabet: list or string with elemnts = letters of the target language
    hashFunction: One of the three hash functions defined below
    Returns a dictionary containing a frequency distribution of all integers
    returned by the hash function.'''
    
    hashedDict = {}

    for w in wordList:
        #Convert each word in the wordList to its corresponding hash.
        hashedWord = hashFunction(alphabet, w)
        
        #Create a frequency distribution of all the integers returned by the hash function.
        hashedDict[hashedWord] = hashedDict.get(hashedWord, 0) + 1
    
    return hashedDict

def firstHashFunction(alphabet,s):
    '''
    alphabet: list or string with elemnts = letters of the target language
    s: word (key) to be hashed
    returns int: the hashed value
    '''
    return alphabet.index(s[0])

def secondHashFunction(alphabet,s):
    '''
    alphabet: list or string with elemnts = letters of the target language
    s: word (key) to be hashed
    returns int: the hashed value
    '''
    return alphabet.index(s[-1])

def thirdHashFunction(alphabet,s):
    '''
    alphabet: list or string with elemnts = letters of the target language
    s: word (key) to be hashed
    returns int: the hashed value
    '''
    total = 0

    for char in s:
        total += alphabet.index(char)
    return total % len(alphabet)
