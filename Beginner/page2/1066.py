even = [] 
odd = []
positive = []
negative = []
numbers = []

for i in range(0, 5):
    numbers.append(int(input()))

even = [n for n in numbers if n%2 == 0]
odd = [n for n in numbers if n%2 != 0]
positive = [n for n in numbers if n > 0]
negative = [n for n in numbers if n < 0]

print(str(len(even)) + ' valor(es) par(es)')
print(str(len(odd)) + ' valor(es) impar(es)')
print(str(len(positive)) + ' valor(es) positivo(s)')
print(str(len(negative)) + ' valor(es) negativo(s)')