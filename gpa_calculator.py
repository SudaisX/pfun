[a,b,c,d] = [int(x) for x in input().strip().split()]

def calc(x):
    if x >= 97 and x <= 100:
        return 'A+', 4
    elif x >= 93 and x <= 97:
        return 'A', 4
    elif x >= 90 and x <= 93:
        return 'A-', 3.67
    elif x >= 80 and x <= 90:
        return 'B+', 3.33
    elif x >= 75 and x <= 80:
        return 'B', 3
    elif x >= 70 and x <= 75:
        return 'B-', 2.67
    elif x >= 67 and x <= 70:
        return 'C+', 2.33
    elif x >= 63 and x <= 67:
        return 'C', 2
    elif x >= 60 and x <= 63:
        return 'C-', 1.67
    else:
        return 'F', 0

def gpa_calculator(a, b, c, d):
    a, apoints = calc(a)
    b, bpoints = calc(b)
    c, cpoints = calc(c)
    d, dpoints = calc(d)

    gpa = (apoints + bpoints + cpoints + dpoints) / 4
    print(f'Your grades are {a} {b} {c} {d}')
    print(f'Your GPA is {gpa}')

gpa_calculator(a,b,c,d)