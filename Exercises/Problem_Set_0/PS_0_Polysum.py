#A regular polygon has n number of sides. Each side has length s.
#The area of a regular polygon is: 0.25*n*s**2 / tan(pi/n)
#The perimeter of a polygon is: length of the boundary of the polygon
#Write a function called polysum that takes 2 arguments, n and s. 
#This function should sum the area and square of the perimeter of the regular polygon. 
#The function returns the sum, rounded to 4 decimal places.

def polysum(n,s):
    '''
    n: int - number of sides of a regular polygon
    s: float - length of side of a regular polygon
    
    This function returns the sum of the area and the square of the perimeter
        of the regular polygon, rounded to 4decimal places.
    '''
    import math
    
    area_polygon = 0.25*n*s**2 / math.tan(math.pi/n)
    perimeter_polygon = n*s
    
    sum_area_sq_perimeter = area_polygon + perimeter_polygon*perimeter_polygon
    
    return round(sum_area_sq_perimeter,4)


