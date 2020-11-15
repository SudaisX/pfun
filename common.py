def common(word1, word2):
    common = ''
    for chr1 in word1:
        for chr2 in word2:
            if chr2 == chr1:
                if chr2 in common:
                    pass
                else:
                    common += chr2
    return(common)

word1 = input()
word2 = input()
print(common(word1, word2))