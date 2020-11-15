def series(n):
    if n < 1:
        return 'n must be greater than 0'
    else:
        if n == 1:
            return 1
        else:
            return series(n-1)*series(n-1) + 1

n=int(input())
print(series(n))