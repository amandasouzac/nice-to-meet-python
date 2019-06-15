import math

N = 3.14159
R = float(input())
A = N * (math.pow(R, 2))

print('A=' + str("%.4f" % round(A, 4)))