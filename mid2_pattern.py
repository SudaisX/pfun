def pattern(n):
    spaces = '  '
    star = '* '
    difference = x - n
    if n == 0:
        print(f'{star * x}')
    elif n > 0:
        if difference == 0:
            return pattern(n-1)
        else:
            print(f'{spaces * n}{star * (difference)}')
            return pattern(n-1)

while True:
    n = int(input())
    x = n
    pattern(n)