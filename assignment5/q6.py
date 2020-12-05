def transmogrify():
    n = int(input())
    l_dict = {}
    for i in range(n):
        letter = input()
        l_dict[letter[0]] = letter[-1]
    
    word = input()
    translated = ''
    for i in range(len(word)):
        translated += l_dict[word[i]]
    return translated

print(transmogrify())