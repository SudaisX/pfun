def bend(size):
    space = '  '
    star = '* '
    
    print(star * size)
    if size == 1:
        pass
    elif size == 2:
        print(star * size)
    else:
        for i in range(size - 2):
            print(f'{star}{space*(i)}{star}{(size - 3 - i)*space}*')
        print(star * size)
        

size = int(input())