L = int(input())
C = input()

matrix = []

for i in range(12):
    line = []

    for j in range(12):
        line.append(float(input()))
    
    matrix.append(line)

vector = matrix[L]
total = sum(vector)

if C == 'S':
    print('%.1f' % total)
else:
    print('%.1f' % (total/12))

