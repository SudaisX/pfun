def breakdown(n):
    if n == 0:
        return []
    elif n > 0 and n < 9:
        return [1] + breakdown(n-1)
    elif n > 9 and n < 99:
        return [10] + breakdown(n-10)
    elif n > 99 and n < 999:
        return [100] + breakdown(n-100)
    elif n > 999 and n < 9999:
        return [1000] + breakdown(n-1000)
    elif n > 9999 and n < 99999:
        return [10000] + breakdown(n-10000)
    
n = int(input())
print(breakdown(n))

