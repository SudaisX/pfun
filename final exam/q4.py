#corpus

def biggest_bucket(corpus):
    words = (''.join([l for l in corpus.lower() if l.isalpha() or l.isspace()])).split()
    
    freq = {chr(i):0 for i in range(97, 123)}
    for word in words:
        freq[word[0]] += 1
        
    highest = 0
    for n in freq.values():
        if n > highest:
            highest = n
            
    return [[i, j] for i, j in freq.items() if j == highest]
print(biggest_bucket(input()))