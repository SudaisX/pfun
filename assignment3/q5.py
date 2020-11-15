def suffixSimilarity(word):
    discard = ''
    suffix = ''
    length = 0
    
    for i in range(len(word)):
        if i == 0:
            length += len(word)
        else:
            discard = discard + word[i-1]
            suffix = word[i:]
            for j in range(len(suffix)):
                if word[j] == suffix[j]:
                    length += 1
                else:
                    break
    return length

s=input()
print(suffixSimilarity(s))