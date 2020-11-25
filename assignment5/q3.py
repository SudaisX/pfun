import math
import os
import random
import re
import sys

def minDiff(arr):
    arr.sort()
    diff, diff_sum = [], 0
    for i in range(len(arr)):
        if i == len(arr) or i == len(arr)-1:
            pass
        else:
            diff.append(abs(arr[i]-arr[i+1]))
            
    for n in diff:
        diff_sum += n   
    return diff_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = minDiff(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
