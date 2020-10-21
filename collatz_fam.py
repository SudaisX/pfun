def verify_collatz(n):
    collatz = ''
    while True:
        collatz += f'{n}, '
        if n == 1 or n == 5 or n == 17:
            print(collatz[0:len(collatz) - 2])
            break
        else:
            if n % 2 == 0:
                n = int(n/2)
            else:
                n = n*3 - 1
        

n = int(input())