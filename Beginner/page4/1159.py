OUT = []

while True:
  x = int(input())
  
  if x == 0:
    break
  
  x = x if x%2 == 0 else x+1
  total = 0
  j = 0

  while (j < 5):
    total += x
    x += 2
    j += 1
  
  OUT.append(total)

for i in OUT:
  print(i)