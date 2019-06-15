points = list(map(float, input().split()))
a = points[0]
b = points[1]
c = points[2]

def verifyTriangle(A, B, C):
    if A + B > C and A + C > B and B + C > A:
        return True
    return False

if verifyTriangle(a, b, c):
    perimeter = a + b + c
    print('Perimetro = ' + '%.1f' % perimeter)
else:
    area = ((a + b)/2) * c
    print('Area = ' + '%.1f' % area)