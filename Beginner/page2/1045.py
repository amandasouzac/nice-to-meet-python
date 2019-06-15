points = list(map(float, input().split()))
points.sort()

a = points[2]
b = points[1]
c = points[0]

def triangleType(A, B, C):
    AA = pow(A, 2)
    BB = pow(B, 2)
    CC = pow(C, 2)

    if AA == BB + CC:
        print('TRIANGULO RETANGULO')
    elif AA > BB + CC:
        print('TRIANGULO OBTUSANGULO')
    else:
        print('TRIANGULO ACUTANGULO')

    if A == B == C:
        print('TRIANGULO EQUILATERO')
    elif A == B or B == C:
        print('TRIANGULO ISOSCELES')


if a >= b + c:
    print('NAO FORMA TRIANGULO')
else:
    triangleType(a, b, c)
