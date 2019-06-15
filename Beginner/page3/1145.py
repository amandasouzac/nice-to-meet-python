[X, Y] = list(map(int, input().split()))

i = 1

while (i <= Y):
    line = []
    for j in range(0, X):
        line.append(str(i))
        i += 1
        if i > Y:
            break
    print(str.join(' ', line))
