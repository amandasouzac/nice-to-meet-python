A = []

for i in range(100):
    A.append(float(input()))

for i in range(100):
    if A[i] <= 10:
        print('A[' + str(i) + '] = ' + '%.1f' % A[i])