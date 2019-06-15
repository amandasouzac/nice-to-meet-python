pi = 3.14159
values = input().split()
A = float(values[0])
B = float(values[1])
C = float(values[2])

triangulo = (A*C)/2
circulo = pi * (pow(C, 2))
trapezio = ((A + B)/2) * C
quadrado = pow(B, 2)
retangulo = A * B

print('TRIANGULO: ' + '%.3f' % triangulo)
print('CIRCULO: ' + '%.3f' % circulo)
print('TRAPEZIO: ' + '%.3f' % trapezio)
print('QUADRADO: ' + '%.3f' % quadrado)
print('RETANGULO: ' + '%.3f' % retangulo)