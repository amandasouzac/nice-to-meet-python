total = 1
x, y = 1, 1

while (x <= 39):
    x += 2 
    y *= 2
    total += x/y

print('%.2f' % total)