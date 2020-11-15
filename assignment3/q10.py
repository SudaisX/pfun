import math
import os
import random
import re
import sys

def isPowerTwo(n):
    if n == 1:
        return True
    elif n == 2:
        return True
    elif n > 2:
        return isPowerTwo(n/2)
    else:
        return False

def isPower(arr):
    powerTwo = []
    for n in arr:
        if isPowerTwo(n):
            powerTwo.append(1)
        else:
            powerTwo.append(0)        
    return powerTwo

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = isPower(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()