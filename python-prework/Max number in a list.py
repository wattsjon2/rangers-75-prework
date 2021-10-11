def max_num_in_list(a_list):                    
    sort_list = sorted(a_list)                  
    maxnum = sort_list.pop()                    
    return(maxnum)                               

print(max_num_in_list([19, 12, 1, 4, 6, 7]))           
print(max_num_in_list([1,2,3,18,4,5,6,7])) 


def max_num_in_list(a_list):                                       
    return(max(a_list)) 
