def random(seed, M, a, b):
    X = [seed]
    for i in range(19):
        Xn = (a*X[-1] + b) % M
        X.append(Xn)
    print(X)

random(420, 577, 13, 89)