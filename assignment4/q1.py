def special_sort(s):
    upper, lower, numeric, special = '', '', '', ''
    
    for char in s:
        if char.isupper():
            upper += char
        elif char.islower():
            lower += char
        elif char.isnumeric():
            numeric += char
        else:
            special += char
            
    upper = ''.join(sorted(upper))
    lower = ''.join(sorted(lower))
    numeric = ''.join(sorted(numeric))
    special = ''.join(sorted(special))
    
    return upper + lower + numeric + special

s = input()

print(special_sort(s))