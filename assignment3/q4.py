def isPangram(word):
    alphas = [0 for i in range(26)]
    word = word.lower()
        
    for i in range(97, 123):
        for char in word:
            if char == chr(i):
                alphas[97-i] += 1
                
    for i in alphas:
        if i < 1:
            return False
    else:
        return True
        
s=input()
print(isPangram(s))