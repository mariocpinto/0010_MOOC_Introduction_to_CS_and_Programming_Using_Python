import matplotlib.pyplot as plt
import math

from hash_functions import *
from helper_functions import *

EN_FILE_PATH = 'C:/Users/Mario/Documents/GitHub/0010_MOOC_Introduction_to_CS_and_Programming_Using_Python/Exercises/Mini_Project/top10000en.txt'
FR_FILE_PATH = 'C:/Users/Mario/Documents/GitHub/0010_MOOC_Introduction_to_CS_and_Programming_Using_Python/Exercises/Mini_Project/top10000fr.txt'
DE_FILE_PATH = 'C:/Users/Mario/Documents/GitHub/0010_MOOC_Introduction_to_CS_and_Programming_Using_Python/Exercises/Mini_Project/top10000de.txt'
NL_FILE_PATH = 'C:/Users/Mario/Documents/GitHub/0010_MOOC_Introduction_to_CS_and_Programming_Using_Python/Exercises/Mini_Project/top10000nl.txt'

# Select HashFunction
HashFunction = thirdHashFunction # firstHashFunction or secondHashFunction or thirdHashFunction
Method = '3rd Hash Function' # This is used in the plot header

# Select Language and File Path
filepath = NL_FILE_PATH # FR_FILE_PATH or EN_FILE_PATH or DE_FILE_PATH or NL_FILE_PATH
Language = 'Dutch' # This is used in the plot header
# Language = 'English' or 'French' or 'German' or 'Dutch'

# Load words
wordList = loadWords(filepath)

# Determine unique letters in the wordlist
alphabet = sorted(LetterFrequency(wordList).keys())

# Hash the words in the wordlist
hashed_dict = Hash(wordList, alphabet, HashFunction)

# Print out the letters contained in wordList
print alphabet

# Plot the hashed values

# selecting a max value rounded to the nearest power of 10
ymax = max(hashed_dict.values())
ymax = ( 10**(len(str(ymax)) - 1)) * math.ceil(ymax / ( 10.0**(len(str(ymax)) - 1)) )

plt.bar(hashed_dict.keys(), hashed_dict.values(), facecolor='#9999ff', edgecolor='white')
plt.ylabel('Number of words')
plt.xlabel('Hash')
plt.title('Hashed Word Frequency Distribution - ' + Language + ' - ' + Method)
plt.axis([0, len(hashed_dict.keys()), 0, ymax ])
plt.show()
