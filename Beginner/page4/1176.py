a = 0
b = 1

for i in range(60):
    c = b + a
    fib.append(c)
    a = b
    b = c

T= int(input())

for i in range(T):
    N = int(input())
    print('Fib(' + str(N) +  ') = '+ str(fib[N]))