X = int(input())
Y = int(input())

maior = X if X > Y else Y
menor = Y if Y < X else X
menor += 1

for i in range(menor, maior):
  rest = i%5
  if rest == 2 or rest == 3:
    print(i)
  