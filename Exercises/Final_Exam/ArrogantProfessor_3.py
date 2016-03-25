class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return 'Prof. ' + self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    
    def lecture(self, stuff):
        return 'It is obvious that I believe that ' + Person.say(self,stuff)

#pe = Professor('eric')
#ae = ArrogantProfessor('eric')
#
#print pe.say('the sky is blue')
## Expected:
##Prof. eric says: I believe that eric says: the sky is blue 
#
#print ae.say('the sky is blue')
## Expected: 
##Prof. eric says: It is obvious that I believe that eric says: the sky is blue 
#
#print ae.lecture('the sky is blue')
## Expected: 
##It is obvious that I believe that eric says: the sky is blue