s = input()
keypad = input()

def entryTime(s,keypad):
    time = 0
    a1 = keypad[0]
    a2 = keypad[1]
    a3 = keypad[2]
    b1 = keypad[3]
    b2 = keypad[4]
    b3 = keypad[5]
    c1 = keypad[6]
    c2 = keypad[7]
    c3 = keypad[8]
    for i in range(len(s)):
        if i == len(s)-1:
            pass
        else:
            if s[i] == a1:
                if s[i+1] == a1 or i == len(s):
                    time = time + 0
                elif s[i+1] == a2 or s[i+1] == b1 or s[i+1] == b2:
                    time = time + 1
                else:
                    time = time + 2
            elif s[i] == a2:
                if s[i+1] == a2 or i == len(s):
                    time = time + 0
                elif s[i+1] == a1 or s[i+1] == b1 or s[i+1] == b2 or s[i+1] == b3 or s[i+1] == a3:
                    time = time + 1
                else:
                    time = time + 2
            elif s[i] == a3:
                if s[i+1] == a3 or i == len(s):
                    time = time + 0
                elif s[i+1] == a2 or s[i+1] == b2 or s[i+1] == b3:
                    time = time + 1
                else:
                    time = time + 2
            elif s[i] == b1:
                if s[i+1] == b1 or i == len(s):
                    time = time + 0
                elif s[i+1] == a1 or s[i+1] == a2 or s[i+1] == b2 or s[i+1] == c1 or s[i+1] == c2:
                    time = time + 1
                else:
                    time = time + 2
            elif s[i] == b2:
                if s[i+1] == b2 or i == len(s):
                    time = time + 0
                else:
                    time = time + 1
            elif s[i] == b3:
                if s[i+1] == b3 or i == len(s):
                    time = time + 0
                elif s[i+1] == a2 or s[i+1] == a3 or s[i+1] == b2 or s[i+1] == c2 or s[i+1] == c3:
                    time = time + 1
                else:
                    time = time + 2
            elif s[i] == c1:
                if s[i+1] == c1 or i == len(s):
                    time = time + 0
                elif s[i+1] == b1 or s[i+1] == b2 or s[i+1] == c2:
                    time = time + 1
                else:
                    time = time + 2
            elif s[i] == c2:
                if s[i+1] == c2 or i == len(s):
                    time = time + 0
                elif s[i+1] == b1 or s[i+1] == b2 or s[i+1] == b3 or s[i+1] == c1 or s[i+1] == c3:
                    time = time + 1
                else:
                    time = time + 2
            elif s[i] == c3:
                if s[i+1] == c3 or i == len(s):
                    time = time + 0
                elif s[i+1] == c2 or s[i+1] == b2 or s[i+1] == b3:
                    time = time + 1
                else:
                    time = time + 2
    return time
        
            
    

print(entryTime(s,keypad))