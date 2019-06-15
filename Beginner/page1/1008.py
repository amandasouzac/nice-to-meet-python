ID = int(input())
hours = int(input())
per_hour = float(input())

salary = hours * per_hour

print('NUMBER = ' + str(ID))
print('SALARY = U$ ' + "%.2f" % salary)