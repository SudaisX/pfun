lyrics = '''I been away, but now I feel you, yeah
Wonder what made you feel like I could be the one, oh ah
Lately, it's been me, I pissed you off
I let you in my feelings, you really feel, yeah
Uh huh, saying
You been high, I get that
I been at the kickback
Nothing will content me
Doesn't matter, ah
Thought you came from nothin'
Trade, I'll ask my cousin
You should like my brother
Doesn't matter, ah
I've had a taste of how you feeling, yeah
Yeah, I've been hiding how I feel for way too long, oh
Lately it's been me, I pissed you off
I let you in my feelings, you really feel, yeah
Uh huh, saying
You been high, I get that
I've been at the kickback
Nothing will content me
Doesn't matter, ah
Thought you came from nothing
Trade, I'll ask my cousin
You should like my brother
Doesn't matter, ah
You been high, I get that
I've been at the kickback
Nothing will content me
Doesn't matter, ah
Thought you came from nothing
Trade, I'll ask my cousin
You should like my brother
Doesn't matter, ah'''

lyrics = lyrics.split()
mydict = {}

for word in lyrics:
    if word in mydict:
        mydict[word] += 1
    else:
        mydict[word] = 1

for lyric in mydict.keys():
    print(f'\"{lyric}\" was repeated {mydict[lyric]} times')