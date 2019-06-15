N = int(input())
odd_sum = []

for i in range(0, N):
    [X, Y] = list(map(int, input().split()))
    maior = X if X > Y else Y
    menor = Y if Y < X else X
    menor += 1

    os = 0
    for j in range(menor, maior):
        if j%2 != 0:
            os += j
    odd_sum.append(os)

for i in odd_sum:
    print(i)
