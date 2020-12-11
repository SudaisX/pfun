msg = input()
def reverse(word):
    word = word.lower()
    new_word = ''
    for i in range(len(word)+1):
        if i != 0:
            if i == 1 and word[-i].isalpha(): 
                new_word += word[-i].upper()
            else:
                new_word += word[-i] 
    return new_word
    
msg = msg.split()
reverse_msg = []
[reverse_msg.append(reverse(word)) for word in msg]
print(' '.join(reverse_msg))