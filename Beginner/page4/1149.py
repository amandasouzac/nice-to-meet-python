values = list(map(int, input().split()))

def findValidN(values):
  for i in values:
    if i > 0:
      return i

A = values.pop(0)
N = findValidN(values)

total = 0
for i in range(A, A+N):
  total += i

print(total)