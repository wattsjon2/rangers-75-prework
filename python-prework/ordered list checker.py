def is_consecutive(a_list):             
    a = 0                                                                      
    while a < len(a_list) -1:              
        if a_list[a + 1] - a_list[a] != 1:            
            break                            
        else:
            a += 1                        
    return(a == len(a_list) - 1)            
    
       
print(is_consecutive([1,2,3,4,5,6]))    
print(is_consecutive([1,3,4,5,6]))

def is_consecutive(a_list):  
    """
    Figure out if all numbers in the given list are consecutive
    """

    return sorted(a_list) == list(range(min(a_list),max(a_list )+ 1))

print(is_consecutive([1,2,3,4,5,6]))    
print(is_consecutive([1,3,4,5,6]))


