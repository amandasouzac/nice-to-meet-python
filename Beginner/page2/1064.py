i = 0
positives = 0
psum = 0

for i in range(0, 6):
    x = float(input())
    if x >= 0:
        positives += 1
        psum += x

average = psum / positives
print(str(positives) + ' valores positivos')
print('%.1f' % average)