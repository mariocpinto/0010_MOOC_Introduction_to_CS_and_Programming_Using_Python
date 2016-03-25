def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    inv_dict = {}
    
    for key,value in d.items():
        inv_dict[value] = sorted(inv_dict.get(value,[]) + [key])
    
    return inv_dict

#d = {1:10, 2:20, 3:30}
#print dict_invert(d)
#
#d = {1:10, 2:20, 3:30, 4:30}
#print dict_invert(d)
#
#d = {4:True, 2:True, 0:True}
#print dict_invert(d)