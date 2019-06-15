item = list(map(int, input().split()))

total = 0

if item[0] == 1:
    total = 4 * item[1]
elif item[0] == 2:
    total = 4.5 * item[1]
elif item[0] == 3:
    total = 5 * item[1]
elif item[0] == 4:
    total = 2 * item[1]
else:
    total = 1.5 * item[1]

print('Total: R$ ' + '%.2f' % total)