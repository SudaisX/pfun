plus, minus, slash, height, width = input().strip().split()
height = int(height)
width = int(width)

space = ' '

def general_grid(plus, minus , slash, height, width):
    
    plus_minus(plus, minus, height, width)
    slash_space(height, width, slash)
    plus_minus(plus, minus, height, width)
    slash_space(height, width, slash)
    plus_minus(plus, minus, height, width)

def plus_minus(plus, minus, height, width):
    l1 = f'{plus} {(minus+space)*width}{plus} {(minus+space)*width}{plus}'
    print(l1)

def slash_space(height, width, slash):
    spaces = (space * width) * 2
    p1 = f'{slash}{spaces} {slash}{spaces} {slash}'
    print((p1 + '\n') * height, end='')
    
general_grid(plus, minus, slash, height, width)