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
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)
    
    def lecture(self, stuff):
        return 'It is obvious that ' + Person.say(self,stuff)

#ae = ArrogantProfessor('eric')
#print ae.say('the sky is blue')
## Expected: 
##eric says: It is obvious that eric says: the sky is blue
#
#print ae.lecture('the sky is blue')
## Expected:
##It is obvious that eric says: the sky is blue