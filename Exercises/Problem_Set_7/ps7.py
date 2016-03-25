import random as rand
import string

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        # Your Code Here
        self.name = name
        self.location = location
        self.species_types = species_types
        
    def get_number_of_species(self, animal):
        # Your Code Here 
            return self.species_types.get(animal,0)

    def get_location(self):
        # Your Code Here 
        return self.location
        
    def get_species_count(self):
        # Your Code Here 
        return self.species_types.copy()
        
    def get_name(self):
        # Your Code Here 
        return self.name
        
    def adopt_pet(self, species):
        # Your Code Here 
        count = self.species_types.get(species,0)
        
        if count == 1:
            del self.species_types[species]
        
        elif count > 1:
            self.species_types[species] = count - 1
    
    def __repr__(self):
        return self.get_name()    

class Adopter:
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        # Your Code Here 
        self.name = name
        self.desired_species = desired_species
        
    def get_name(self):
        # Your Code Here 
        return self.name
        
    def get_desired_species(self):
        # Your Code Here 
        return self.desired_species
        
    def get_score(self, adoption_center):
        # Your Code Here 
        return float(adoption_center.get_number_of_species(self.desired_species))

    def __repr__(self):
        return self.get_name()

class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species = considered_species
        
    def get_score(self, adoption_center):
        return max(0.0, Adopter.get_score(self,adoption_center) + \
            0.3*sum([ adoption_center.get_number_of_species(species) for species in self.considered_species]))


class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        self.feared_species = feared_species        

    def get_score(self, adoption_center):
        return max(0.0, Adopter.get_score(self, adoption_center) - \
            0.3*adoption_center.get_number_of_species(self.feared_species))


class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species       
    
    def get_score(self, adoption_center):
        return 0.0 if sum([ adoption_center.get_number_of_species(species) for species in self.allergic_species]) \
                else Adopter.get_score(self, adoption_center)

class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        self.medicine_effectiveness = medicine_effectiveness
        
    def get_score(self, adoption_center):
        return Adopter.get_score(self, adoption_center) * \
            min( [1.0] + [ self.medicine_effectiveness[species] for species in \
            list(set(adoption_center.get_species_count().keys()).intersection(self.allergic_species )) ] )
            
#maa = MedicatedAllergicAdopter('Alice','dog',['cat','rat'],{'cat':0.9, 'rat':0.8})
#ac = AdoptionCenter('Adoption Home', {'dog':3, 'cat':5, 'donkey':3}, (1.0,2.0))
#
#print maa.get_score(ac)

class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        # assert -5.0 <= location[0] and location[0]<= 5.0
        # assert -5.0 <= location[1] and location[1]<= 5.0
        self.location = location
        
    def get_linear_distance(self, to_location):
        x1 = self.location[0]
        y1 = self.location[1]
        x2 = to_location[0]
        y2 = to_location[1]
        
        return ( (x2 - x1)**2 + (y2 - y1)**2 )**0.5
    
    def get_score(self, adoption_center):
        dist = self.get_linear_distance(adoption_center.get_location())
        
        if dist < 1:
            return adoption_center.get_number_of_species(self.desired_species)
        
        elif dist < 3:
            return rand.uniform(0.7,0.9)*adoption_center.get_number_of_species(self.desired_species)
        
        elif dist < 5:
            return rand.uniform(0.5,0.7)*adoption_center.get_number_of_species(self.desired_species)
        
        else:
            return rand.uniform(0.1,0.5)*adoption_center.get_number_of_species(self.desired_species)
    
def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    # Your Code Here 
      
    # Sort by score, then by name
    list_of_adoption_centers.sort(key=lambda ac : (-adopter.get_score(ac), ac.get_name()))
    
    return list_of_adoption_centers
    
#a = Adopter('Me','Dog')
#ac1 = AdoptionCenter('AC1',{'Dog':1,'Cat':2}, (1.0,1.0))
#aa2 = AdoptionCenter('AA2',{'Dog':1,'Cat':3}, (2.0,2.0))
#ac3 = AdoptionCenter('AC3',{'Dog':2,'Cat':2}, (3.0,3.0))
#list_of_adoption_centers = [ac1, aa2, ac3]
#
#print get_ordered_adoption_center_list(a, list_of_adoption_centers)


def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    # Your Code Here 
    
    # Sort by score, then by name
    list_of_adopters.sort(key = lambda a: (-a.get_score(adoption_center), a.get_name()) )
    
    return list_of_adopters[:n]

#ac = AdoptionCenter('AC',{'Dog':1,'Cat':4, 'Goat':3, 'Bull':4}, (1.0,1.0))
#a1 = Adopter('A1','Dog')
#a2 = Adopter('A2','Cat')
#a3 = Adopter('A3','Bull')
#
#print get_adopters_for_advertisement(ac, [a1, a2, a3], 5)
    
