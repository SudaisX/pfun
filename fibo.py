def fib_over(r):
    a = 0
    b = 1
    sum = 0
    while True:
        a = b
        b = sum
        sum = a + b
        #print(sum)
        if sum > r:
            return(sum)

lb = int(input())
print(fib_over(lb))