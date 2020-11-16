def random(seed, M, a, b):
    X = [seed]
    for i in range(19):
        Xn = (a*X[-1] + b) % M
        X.append(Xn)
    print(X)

M = 577
a = 13
b = 89
seed = 420
random(seed, M, a, b)