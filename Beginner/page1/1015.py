import math

point1 = list(map(float, input().split()))
point2 = list(map(float, input().split()))

distance = math.sqrt(pow( point2[0] - point1[0],2) + pow(point2[1] - point1[1], 2))
print('%.4f'%distance)