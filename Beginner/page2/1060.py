i = 0
positives = 0

for i in range(0, 6):
    x = float(input())
    if x >= 0:
        positives += 1

print(str(positives) + ' valores positivos')