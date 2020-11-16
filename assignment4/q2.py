import math
import os
def diagonalDifference(arr):
    rows, diag1, diag2 = len(arr), 0, 0

    for i in range(rows):
        diag1 += arr[i][i]
        diag2 += arr[i][-i-1]
        
    return abs(diag2 - diag1)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()