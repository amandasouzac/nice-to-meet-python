N = int(input())
OUT = []

for i in range(0, N):
    x = int(input())
    s = ''
    if x == 0:
        s = 'NULL'
    else:
        if x%2 == 0:
            s = 'EVEN '
        else:
            s = 'ODD '
        
        if x > 0:
            s += 'POSITIVE'
        else:
            s += 'NEGATIVE'

    OUT.append(s)

for s in OUT:
    print(s)