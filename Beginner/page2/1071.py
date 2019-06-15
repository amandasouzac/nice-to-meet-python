A = int(input())
B = int(input())
soma = 0

maior = A if A > B else B
menor = B if B < A else A
menor += 1

while (menor < maior):
    if(menor % 2 != 0):
        soma += menor
    menor+=1

print(soma)