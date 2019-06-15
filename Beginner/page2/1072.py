N = int(input())
numbers = []

for i in range(0, N):
    numbers.append(int(input()))

IN = len([n for n in numbers if n >= 10 and n <=20])
OUT = len(numbers) - IN

print(str(IN) + ' in')
print(str(OUT) + ' out')