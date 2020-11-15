def u_comes_after_t(word):
    if len(word) > 1:
        if word.find('u') > word.find('t'):
            return True
        else:
            return False
    else:
        return False
word = input()
print(u_comes_after_t(word))