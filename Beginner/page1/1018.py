banknotes = [100, 50, 20, 10, 5, 2, 1]

N = int(input())

print(str(N))

for X in banknotes:
    qtd = int(N/X)
    print(str(qtd) + ' nota(s) de R$ ' + str(X) + ',00')
    N = N - (qtd * X)

