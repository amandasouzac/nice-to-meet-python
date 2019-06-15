N = int(input())
OUT = []

for i in range(N):
    X = int(input())
    flag = 0

    for j in range (2, X):
        if X%j == 0:
            flag = 1
            break
    
    if flag == 1:
        OUT.append(str(X) + ' nao eh primo')
    else:
        OUT.append(str(X) + ' eh primo')

for s in OUT:
    print(s)