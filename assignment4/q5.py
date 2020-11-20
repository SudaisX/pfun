def partition_modulo_n(n, t):
    negative = False
    if n < 0:
        negative = True
        n = -n
        
    remainders = [[i for i in t if i % n == j] for j in range(n)]
    
    if negative == True:
        return {-i:remainders[-i] for i in range(n)}
    else:
        return {i:remainders[i] for i in range(n)}
    
from pprint import pprint
n = int(input().strip())
t = [int(i) for i in input().strip().split()]
pprint(partition_modulo_n(n, t))
pprint(t)
