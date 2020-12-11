#no pairs allowed

import math
import os
import random
import re
import sys

def minimalOperations(words):
    changes = [0 for i in range(len(words))]
    words = [list(word) for word in words]
    for word in range(len(words)):
        length = len(words[word])
        for l in range(length):
            if l < length-1:
                if words[word][l] == words[word][l+1]:
                    words[word][l+1] = '!'
                    changes[word] += 1
    return changes


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    words_count = int(input().strip())

    words = []

    for _ in range(words_count):
        words_item = input()
        words.append(words_item)

    result = minimalOperations(words)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
