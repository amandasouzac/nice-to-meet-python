N = int(input())
OUT = []

for i in range(N):
  [x,y] = list(map(int, input().split()))
  x = x if x%2 != 0 else x+1
  total = 0
  j = 0

  while (j < y):
    total += x
    x += 2
    j += 1

  OUT.append(total)

for i in OUT:
  print(i)