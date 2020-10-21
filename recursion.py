def countdown(n):
    count = ''
    if n == 1:
        print(n, end= ', ')
    else:
        countdown(n - 1)
        print(f'{n}, ', end='')

countdown(5)