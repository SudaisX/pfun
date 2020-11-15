def convertToList(keypad):
    temp = [[0 for col in range(3)] for row in range(3)]
    for i in range(3):
        temp[0][i] = keypad[i]
        temp[1][i] = keypad[i+3]
        temp[2][i] = keypad[i+6]
    return temp

def findIndex(keypad, n):
    for i in range(3):
        for j in range(3):
            if keypad[i][j] == n:
                return i, j

def keyDistance(nextRow, nextCol, keyRow, keyCol):
    if abs(nextRow-keyRow) == 0 and abs(nextCol-keyCol) == 0:
        return 0
    elif abs(nextRow-keyRow) == 1 and (abs(nextCol-keyCol) == 1 or abs(nextCol-keyCol) == 0):
        return 1
    elif (abs(nextRow-keyRow) == 0 or abs(nextRow-keyRow) == 1) and abs(nextCol-keyCol) == 1:
        return 1
    else:
        return 2
    
def entryTime(s, keypad):
    time = 0
    keypad = convertToList(keypad)
    for i in range(len(s)):
        if i == len(s) or i == len(s)-1:
            pass
        else:
            keyRow, keyCol = findIndex(keypad, s[i])
            nextRow, nextCol = findIndex(keypad, s[i+1])
            d = keyDistance(nextRow, nextCol, keyRow, keyCol)
            time += d
    
    return(time)
              
s = input()
keypad = input()
print(entryTime(s,keypad))