N = []

for i in range(20):
    N.append(int(input()))

i = 0
j = len(N) - 1

while (i < j):
    aux = N[j]
    N[j] = N[i]
    N[i] = aux

    i += 1
    j -= 1

for i in range(len(N)):
    print('N[' + str(i) + '] = ' + str(N[i]))