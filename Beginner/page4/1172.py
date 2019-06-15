IN = []

for i in range(10):
    x = int(input())
    x = x if x > 0 else 1
    IN.append(x)

for i in range(0, 10):
    print('X[' + str(i) + '] = ' + str(IN[i]))
