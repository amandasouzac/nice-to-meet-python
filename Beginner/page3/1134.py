op = int(input())
alcohol = 0
gasoline = 0
diesel = 0

while (op != 4):
  if op == 1:
    alcohol += 1
  elif op == 2:
    gasoline += 1
  elif op == 3:
    diesel += 1
  op = int(input())

print('MUITO OBRIGADO')
print('Alcool: ' + str(alcohol))
print('Gasolina: ' + str(gasoline))
print('Diesel: ' + str(diesel))