#euclid's algorithm
def gcd(a, b):
    if a == 0:
        return b
    r = b % a
    return gcd(r, a)
   
a = int(input())
b = int(input())