N = int(input())

i = 0
while i < 1000:
    for j in range(N):
        print('N[' + str(i) + '] = ' + str(j))
        i += 1
        if i >= 1000:
            break