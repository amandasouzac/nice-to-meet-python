import math

N = int(input())
OUT = []

for i in range(N):
  [A, B, GA, GB] = list(map(float, input().split()))
  years = 0

  while True:
    years += 1

    if years > 100:
      OUT.append('Mais de 1 seculo.')
      break
    
    A += math.floor(A * GA / 100)
    B += math.floor(B * GB / 100)

    if A > B:
      OUT.append(str(years) + ' anos.')
      break
    
for i in OUT:
  print(i)
