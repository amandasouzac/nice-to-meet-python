X = int(input())
Y = X - 1

while (Y <= X):
  Y = int(input())

total = 0
count = 0

for i in range(X, Y):
  total += i
  count += 1
  if total > Y:
    break

print(count)
