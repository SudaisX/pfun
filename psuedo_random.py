def random(seed):
    M = 577
    a = 13
    b = 89
    X = [seed]
    for i in range(19):
        Xn = (a*X[-1] + b) % M
        X.append(Xn)
    return X

print(random(420))