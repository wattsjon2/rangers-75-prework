def is_leap_year(a_year):           
    if a_year % 4 == 0:             
        if a_year % 100 == 0:       
            if a_year % 400 == 0:   
                leap_year = True       
            else:
                leap_year = False      
        else:
            leap_year = True          
    else:
        leap_year = False            
    return leap_year
    
print(is_leap_year(2000))          # divisible by 4, 100 and 400        
print(is_leap_year(2001))          # not divisible by 4       
print(is_leap_year(2004))          # divisible by 4, not 100        
print(is_leap_year(1900))          # divisible by 4 and 100 but not 400


def is_leap_year(a_year):