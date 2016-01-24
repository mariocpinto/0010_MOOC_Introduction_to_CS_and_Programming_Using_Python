#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s. 
#For example, if s = 'azcbobobegghakl', then your program should print
#
#Number of times bob occurs is: 2
#s = 'azcbobobegghaklbob'

num_of_bobs = 0

for i in range(0,len(s)-2): # -2 since the string 'bob' is of length 3
    if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
        num_of_bobs += 1
        
print 'Number of times bob occurs is:', num_of_bobs