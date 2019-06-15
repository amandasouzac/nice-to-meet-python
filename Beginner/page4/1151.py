def printFib(n):
    s_out = ['0']
    x, y = 0, 1
    while n > len(s_out):
        s_out.append(str(y))
        x, y = y, x+y
    return s_out

N = int(input())
s_out = printFib(N)
print(str.join(' ', s_out))