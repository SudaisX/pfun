s = int(input())

def print_plus_and_equals(size):
    space_size = int(size/2) - 1

    print(((space_size * ' ' + '*' * 2 + '\n') * space_size), end='')
    #for i in range(space_size):
    #    print(space_size * ' ' + '*' * 2)
    
    print(('*' * size + '\n') * 2, end='')
    #for i in range(2):
    #    print('*' * size)
    
    print(((space_size * ' ' + '*' * 2 + '\n') * space_size), end='')
    #for i in range(space_size):
    #    print(space_size * ' ' + '*' * 2)

    print("\n" * space_size)
    print('*' * size, end='')
    print("\n" * 2)
    print('*' * size)

print_plus_and_equals(s)
