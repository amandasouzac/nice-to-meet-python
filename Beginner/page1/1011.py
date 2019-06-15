#  (4/3) * pi * R^3
import math

pi = 3.14159
R = float(input())

volume = (4.0/3) * pi * math.pow(R, 3)

print('VOLUME = ' + '%.3f' % volume)