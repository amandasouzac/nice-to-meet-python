salary = float(input())
p = 0

if salary <= 400:
    p = 15
elif salary > 400 and salary <= 800:
    p = 12
elif salary > 800 and salary <= 1200:
    p = 10
elif salary > 1200 and salary <= 2000:
    p = 7
else:
    p = 4

diff = salary * p / 100.0
new_salary = salary + diff

print('Novo salario: ' + '%.2f' % new_salary)
print('Reajuste ganho: ' + '%.2f' % diff)
print('Em percentual: ' + str(p) + ' %')