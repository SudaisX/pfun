def biggest_bucket(corpus):
    words = (''.join([letter for letter in corpus.lower() if letter.isalpha() or letter.isspace()])).split()
    
    freq = {chr(i):0 for i in range(97, 123)}
    for word in words:
        freq[word[0]] += 1
      
    highest_val = 0
    for i in freq.values():
        if i > highest_val:
            highest_val = i
            
    return [[i, j] for i, j in freq.items() if j == highest_val]

print(biggest_bucket(input()))