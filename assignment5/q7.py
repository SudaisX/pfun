def distance(p1, p2):
    return ((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)**0.5
    
in1 = eval(input())
in2 = eval(input())
print(distance(in1, in2))