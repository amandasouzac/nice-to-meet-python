X = int(input())
Y = int(input())

maior = X if X > Y else Y
menor = Y if Y < X else X

maior += 1
total = 0

for i in range(menor, maior):
  if i%13 != 0:
    total += i
  
print(total)