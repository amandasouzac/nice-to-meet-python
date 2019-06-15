N = int(input())

OUT = [N]

for i in range(10):
    N *= 2
    OUT.append(N) 


for i in range(10):
    print('N[' + str(i) + '] = ' + str(OUT[i]))
