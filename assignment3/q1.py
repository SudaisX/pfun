def rotate(s, n):
    if n >= 0:
        if n > len(s):
            return rotate(s, (n-len(s)))
        else:
            return s[n:len(s)] + s[0:n]
    else:
        if -n > len(s):
            return rotate(s, (n+len(s)))
        else:
            return s[n:] + s[:len(s)+n]
    

s = input().strip()
n = int(input().strip())
print(rotate(s, n))