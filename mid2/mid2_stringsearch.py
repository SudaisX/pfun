#non recursive
def my_find2(s, subs):
    if subs in s:
        return s.find(subs)
    else:
        return -1

#recursion
def find_index(s, subs):
    if subs == s[:len(subs)]:
        return 0
    else:
        s = s[1:]
        if len(s) >= len(subs):
            return 1 + find_index(s, subs)

def my_find(s, subs):
    if subs not in s:
        return -1
    else:
        return find_index(s, subs)


s = input()
subs = input()
print(my_find(s, subs))
