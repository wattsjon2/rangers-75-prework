def oddnums100():
                                                         
    numcheck = 1                        
    oddnum = []
    while len(oddnum) < 100:            
        if numcheck % 2 == 1:          
            oddnum.append(numcheck)     
        numcheck += 1     
    return(oddnum)                      

print(oddnums100())

def add100():
    return([value for value in range(1,200,2)])

print(add100())

