OUT = []

while True:
    [M, N] = list(map(int, input().split()))
    
    if M == N:
        break
    
    if M > N:
        OUT.append('Decrescente')
    else:
        OUT.append('Crescente')


for i in OUT:
    print(i)