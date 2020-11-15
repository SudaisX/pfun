word = input() 
        
def unweave(word):
    half1 = ''
    half2 = ''
    for i in range(0, len(word), 2):
        half1 += word[i]
        if i == len(word) or i == len(word) -1 :
            pass
        else:
            half2 += word[i + 1]
    return half1 + half2

print(unweave(word))