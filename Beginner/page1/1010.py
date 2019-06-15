prod1 = list(map(float, input().split()))
prod2 = list(map(float, input().split()))

total = (prod1[1] * prod1[2]) + (prod2[1] * prod2[2])

print('VALOR A PAGAR: R$ ' + '%.2f' % total)