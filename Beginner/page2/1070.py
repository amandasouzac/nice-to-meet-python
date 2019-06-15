n = int(input())
count = 0

for i in range(n, 1000):
    if i%2 != 0:
        print(i)
        count += 1
    if count >= 6:
        break
