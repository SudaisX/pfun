def encode(string, key):
    for l in range(len(string)):
        lvalue = ord(string[l])
        alphaupper = (lvalue >= 65 and lvalue <= 90)
        alphalower = (lvalue >= 97 and lvalue <= 122)
        d = ord(string[l]) + key
        if alphaupper:
            if d > 90:
                d = d - 90
                newl = chr(d + 64)
                print(newl.upper(), end='')
            else:
                newl = chr(d)
                print(newl.upper(), end='')
        elif alphalower:
            if d > 122:
                d = d - 122
                newl = chr(d + 96)
                print(newl.upper(), end='')
            else:
                newl = chr(d)
                print(newl.upper(), end='')
        else:
            print(string[l], end='')

def decode(string, key):
    for l in range(len(string)):
        lvalue = ord(string[l])
        alphaupper = (lvalue >= 65 and lvalue <= 90)
        alphalower = (lvalue >= 97 and lvalue <= 122)
        d = ord(string[l]) - key
        if alphaupper:
            if d < 65:
                d = 65 - d
                newl = chr(89 - d)
                print(newl.upper(), end='')
            else:
                newl = chr(d)
                print(newl.upper(), end='')
        elif alphalower:
            if d < 97:
                d = 97 - d
                newl = chr(121 - d)
                print(newl.upper(), end='')
            else:
                newl = chr(d)
                print(newl.upper(), end='')
        else:
            print(string[l], end='')

select = input()
string = input()
key = int(input())
if select == '1':
    encode(string, key)
elif select == '2':
    decode(string, key)
