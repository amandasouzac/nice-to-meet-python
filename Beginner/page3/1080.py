numbers = []

for i in range(0, 100):
    numbers.append(int(input()))

m = max(numbers)
print(m)
print(str(numbers.index(m) + 1))