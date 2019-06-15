N = int(input())
OUT = []

for i in range(N):
    X = int(input())
    total = 0

    for j in range (1, X):
        if X%j == 0:
            total += j
    
    if total == X:
        OUT.append(str(X) + ' eh perfeito')
    else:
        OUT.append(str(X) + ' nao eh perfeito')

for s in OUT:
    print(s)