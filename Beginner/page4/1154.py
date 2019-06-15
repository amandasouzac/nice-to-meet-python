all_ages = []

while True:
    age = int(input())
    if age < 0:
        break
    all_ages.append(age)

average = sum(all_ages) / len(all_ages)
print('%.2f' % average) 
    