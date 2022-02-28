from math import log2

def score(ll, N, G):
    return ll - (log2(N)/2)*G

print(score(-32.4, 64, 11))
print(score(-28.3, 64, 15))
print(score(-15.2, 64, 19))


