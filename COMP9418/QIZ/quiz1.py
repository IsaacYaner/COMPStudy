valueSet = [False, True]
for a in range(0, 2):
    for b in range(0, 2):
        gamma = valueSet[a]
        C = valueSet[b]
        print(a, b, (gamma or C)and(gamma or not(C)))