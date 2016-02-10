def nfruits(Init_Fruits, Fruits_Eaten):
    '''
    Init_Fruits: Non-empty dictionary containing type of fruit, quantity pairs
    Fruits_Eaten: String containing sequence of fruits eaten.
    
    Returned value: Maximum count of any fruit when Python reaches campus
    '''
    
    #For all fruits eaten except last
    for fruit in Fruits_Eaten[:-1]:
       
       # Python eats a fruit         
        Init_Fruits[fruit] -= 2 
       # Decremented by 2 since in the next step, all fruits are going to be increased by 1
       #   including the one eaten. 

       # Buy fruits:
        for item in Init_Fruits:
            Init_Fruits[item] += 1
      
    # For the last fruit, Python only eats a fruit, but does not buy anything:
    Init_Fruits[Fruits_Eaten[-1]] -= 1
          
    # Return max of values in Init_Fruits
    return max(Init_Fruits.values())
