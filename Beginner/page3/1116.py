N = int(input())
results = []


for i in range(0, N):
    [X, Y] = list(map(int, input().split()))

    if Y == 0:
        results.append('divisao impossivel')
    else:
        results.append('%.1f'% (X/Y))

for i in results:
    print(i)
