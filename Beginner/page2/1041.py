coordinates = list(map(float, input().split()))
x = coordinates[0]
y = coordinates[1]

if (x == 0 or y == 0):
    if (x == 0 and y == 0):
        print('Origem')
    elif (x == 0):
        print('Eixo Y')
    else:
        print('Eixo X')
else:
    if (x > 0):
        if(y > 0):
            print('Q1')
        else:
            print('Q4')
    else:
        if(y > 0):
            print('Q2')
        else:
            print('Q3')

