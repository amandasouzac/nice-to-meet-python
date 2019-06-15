notes = [100, 50, 20, 10, 5, 2]
coins = [1, 0.5, 0.25, 0.10, 0.05, 0.01]

N = float(input()) + 0.001

print('NOTAS:')
for X in notes:
    qtd = int(N/X)
    print(str(qtd) + ' nota(s) de R$ ' + str(X) + '.00')
    N = N - (qtd * X)

print('MOEDAS:')
for Y in coins:
    qtd = int(N/Y)
    print(str(qtd) + ' moeda(s) de R$ ' + '%.2f' % Y)
    N = N - (qtd * Y)