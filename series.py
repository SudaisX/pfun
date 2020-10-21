def series_x(n):
        if n == 1:
            return 1
        else:
            return 1 + series_x(n-1)*series_x(n-1)

def series(n):
    if n < 1:
        return 'n must be greater than 0'
    elif (n - int(n)) > 0:
        return 'n must be an integer'
    else:
        return series_x(int(n))

n = float(input())
print(series(n))