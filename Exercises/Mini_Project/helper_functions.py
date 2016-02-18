import string

def loadWords(filepath):
    '''
    filepath: string containing path of file to be loaded
    Returns a list containing the words from FILE_PATH
    '''
    fh = open(filepath, 'r')
    wordList = []
    for line in fh:
        wordList.append(line.strip().lower().translate(None, string.punctuation))
    return wordList
    fh.close()

def LetterFrequency(wordList):
    '''
    wordList: list of words
    returns letter_freq: Dictionary with keys = letters contained in words 
                      and values = frequency of letters
    '''
    
    letter_freq = {}
    
    for word in wordList:
        for letter in word:
            letter_freq[letter] = letter_freq.get(letter,0) + 1
    
    return letter_freq