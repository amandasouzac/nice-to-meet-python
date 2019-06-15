values = list(map(int, input().split()))

aux = []

for k in values:
    aux.append(k)

aux.sort()

for i in aux:
    print(str(i))

print()

for j in values:
    print(str(j))