import math

values = list(map(float, input().split()))

a = values[0]
b = values[1]
c = values[2]

delta = pow(b, 2) + ((-1)*4*a*c)

if (delta <= 0 or a == 0):
    print('Impossivel calcular')
else:
    R1 = ((-1)*b + math.sqrt(delta)) / (2*a)
    R2 = ((-1)*b - math.sqrt(delta)) / (2*a)
    print('R1 = ' + '%.5f' % R1)
    print('R2 = ' + '%.5f' % R2)