#Write a program that counts up the number of vowels contained in the string s. 
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
#For example, if s = 'azcbobobegghakl', your program should print:
#
#Number of vowels: 5
#
#s = 'azcbobobegghakl'

num_of_vowels = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')

print 'Number of vowels:', num_of_vowels