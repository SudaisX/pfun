#dot_product
import math

def get_vector(v):
    return tuple(v)

def get_length(v):
    return math.sqrt(sum([n**2 for n in v]))

def dot_product(v1, v2):
    if len(v1) == len(v2):
        return sum([(v1[n]*v2[n]) for n in range(len(v1))])
    else:
        return 'Lengths of the two vectors must be same'

v1 = get_vector(eval(input()))
v2 = get_vector(eval(input()))
print(f'V1 Length: {get_length(v1)}')
print(f'V2 Length: {get_length(v2)}')
print(f'Dot Product(V1,V2): {dot_product(v1, v2)}')