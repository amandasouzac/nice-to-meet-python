table = [[61, 'Brasilia'],[71, 'Salvador'],[11, 'Sao Paulo'],[21, 'Rio de Janeiro'],[32, 'Juiz de Fora'],[19, 'Campinas'],[27, 'Vitoria'],[31, 'Belo Horizonte']]

ddd = int(input())
flag = 0

for x in table:
    if (x[0] == ddd):
        print(x[1])
        flag = 1
        break

if flag == 0:
    print('DDD nao cadastrado')