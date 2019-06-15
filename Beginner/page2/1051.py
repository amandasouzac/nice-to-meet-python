salary = float(input())

taxes = 0

if salary <= 2000:
    print('Isento')
else:
    if salary > 4500:
        x = salary - 4500
        taxes += x  * 28 / 100
        salary = salary - x
    if salary > 3000:
        x = salary - 3000
        taxes += x * 18 / 100
        salary = salary - x
    if salary > 2000:
        x = salary - 2000
        taxes += x * 8 / 100
        salary = salary - x
    print('R$ ' + '%.2f' % taxes)
