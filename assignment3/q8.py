def counting(p, q):
    if q > p:
        return [i for i in range(p, q+1)]
    else:
        return [i for i in range(p, q-1, -1)]
    
p = int(input())
q = int(input())
print(counting(p, q))