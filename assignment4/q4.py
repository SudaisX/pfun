def partition_modulo_three(t):
    zero = [i for i in t if i % 3 == 0]
    one = [i for i in t if i % 3 == 1]
    two = [i for i in t if i % 3 == 2]
    return {0:zero, 1:one, 2:two}

def partition_modulo_three_v2(t):
    remainders = [[i for i in t if i % 3 == j] for j in range(3)]
    return {i:remainders[i] for i in range(3)}

from pprint import pprint
t = [int(i) for i in input().strip().split()]
pprint(partition_modulo_three(t))