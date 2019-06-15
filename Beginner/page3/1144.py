N = int(input())


for i in range(1, N+1):
    p2 = pow(i, 2)
    p3 = pow(i, 3)
    print('%d %d %d' % (i, p2, p3))
    print('%d %d %d' % (i, p2 + 1, p3 + 1))