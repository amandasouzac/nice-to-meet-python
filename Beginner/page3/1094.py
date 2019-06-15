N = int(input())
C = []
R = []
S = []

total_c = 0
total_r = 0
total_s = 0
total = 0

for i in range(0, N):
    animal = input().split()
    if animal[1] == 'C':
        C.append(int(animal[0]))
    elif animal[1] == 'R':
        R.append(int(animal[0]))
    else:
        S.append(int(animal[0]))

total_c = sum(C)
total_r = sum(R)
total_s = sum(S)
total = total_c + total_r + total_s

print('Total: ' + str(total) + ' cobaias')
print('Total de coelhos: ' + str(total_c))
print('Total de ratos: ' + str(total_r))
print('Total de sapos: ' + str(total_s))
print('Percentual de coelhos: ' + '%.2f' % (total_c / total * 100) + ' %')
print('Percentual de ratos: ' + '%.2f' % (total_r / total * 100) + ' %')
print('Percentual de sapos: ' + '%.2f' % (total_s / total * 100) + ' %')
