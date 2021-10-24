xn = 2
p = [[] for i in range(xn)]
p[0].append(0.5)
p[1].append(0.5)
T = [[] for i in range(xn)]
T[0].append(0.5)
T[0].append(0.5)
T[1].append(0.8)
T[1].append(0.2)
en = 2
E = [[] for i in range(en)]
E[0].append(0.4)
E[0].append(0.6)
E[1].append(0.3)
E[1].append(0.7)
e = []
e.append(0)
e.append(1)
e.append(0)
tn = 2
for t in range(1, tn+1):
    for x in range(xn):
        p[x].append(0)
        for x1 in range(xn):
            p[x][t] = p[x][t] + p[x1][t-1] * T[x1][x]
        p[x][t] = p[x][t] * E[x][e[t]]

for i in range(1, tn+1):
    sumi = 0
    for j in range(xn):
        sumi += p[j][i]
    for j in range(xn):
        p[j][i] /= sumi

print(T)
print(E)
print(e)
print(p)
