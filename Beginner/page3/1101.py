OUT = []

while True:
    [M, N] = list(map(int, input().split()))
    
    if M <= 0 or N <= 0:
        break
    
    maior = M if M > N else N
    menor = N if N < M else M
    maior += 1
    
    mn_sum = 0
    mn_string = ''

    for i in range(menor, maior):
        mn_string += str(i) + ' '
        mn_sum += i

    mn_string += ('Sum=' + str(mn_sum)); 
    OUT.append(mn_string)

for i in OUT:
    print(i)

