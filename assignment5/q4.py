import math
import os
import random
import re
import sys


def minX(arr):
    rolling_sum, x = 0, 0
    for n in arr:
        rolling_sum += n
        if rolling_sum < 1:
            x += (1-rolling_sum)
            rolling_sum = 1
    return x
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_count = int(input().strip())
    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = minX(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
