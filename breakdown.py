def breakdown(n):
    negative = False
    if n < 0:
        negative = True
        n = -n

    bList = []
    units = list(str(n))
    length = len(str(n))
    for (i) in units:
        bList += [(10**(length-1))] * int(i)
        length -= 1
        
    if negative == False:
        return bList
    else:
        return [-i for i in bList]
    
n = int(input())
print(breakdown(n))
