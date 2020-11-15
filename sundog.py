def sundog(s):
    length = len(s)
    half = int(length/2)
    if length == 1:
        return s
    elif length % 2 == 0:
        #return f'{sundog(s[:half])} {s} {sundog(s[half:])}'
        return sundog(s[:half]) + ' ' + s + ' ' + sundog(s[half:])
    elif length % 2 != 0:
        #return f'{sundog(s[:half])} {s} {sundog(s[half+1:])}'
        return sundog(s[:half]) + ' ' + s + ' ' + sundog(s[half+1:])

s = 'SUNDOG'
print(sundog(s))