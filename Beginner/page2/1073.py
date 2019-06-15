N = int(input())

for i in range(1, N+1):
    if i%2 == 0:
        x = pow(i, 2)
        print(str(i) + '^2 = ' + str(x))