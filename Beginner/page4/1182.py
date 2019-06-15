C = int(input())
S = input()

matrix = []

for i in range(12):
    line = []

    for j in range(12):
        line.append(float(input()))
    
    matrix.append(line)

vector = []
for v in matrix:
    vector.append(v[C])

total = sum(vector)

if S == 'S':
    print('%.1f' % total)
else:
    print('%.1f' % (total/12))

