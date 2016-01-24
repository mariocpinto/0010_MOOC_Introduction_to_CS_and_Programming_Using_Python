##A catering company has hired you to help with organizing and preparing customer's orders. 
#You are given a list of each customer's desired items, 
#    and must write a program that will count the number of each items needed for the chefs to prepare. 
#The items that a customer can order are: salad, hamburger, and water.
#
#Write a function called item_order that takes as input a string named order. 
#The string contains only words for the items the customer can order separated by one space. 
#The function returns a string that counts the number of each item 
#    and consolidates them in the following order: 
#salad:[# salad] hamburger:[# hambruger] water:[# water]
#
#If an order does not contain an item, then the count for that item is 0. 
#Notice that each item is formatted as 
#[name of the item][a colon symbol][count of the item] 
# and all item groups are separated by a space.
#
#For example:
#
#If order = "salad water hamburger salad hamburger"
#    then the function returns "salad:2 hamburger:2 water:1"
#If order = "hamburger water hamburger" 
#    then the function returns "salad:0 hamburger:2 water:1"

def item_order(order):
    '''
    order is a string that contains the words salad hamburger and water
        any number of times and in any order. 
    Each wordis separated from the other by a space.
    The function returns a string of form:
        salad:<salad_count> hamburger:<hamburger_count> water:<water_count>
    '''
    
    salad_count = order.count('salad')
    hamburger_count = order.count('hamburger')
    water_count = order.count('water')
    
    order_summary = 'salad:' + str(salad_count) + \
                    ' hamburger:' + str(hamburger_count) + \
                    ' water:' + str(water_count)
                    
    return order_summary
    
#my_order = item_order('salad water hamburger salad hamburger')
#print my_order
#my_order = item_order('hamburger water hamburger')
#print my_order
