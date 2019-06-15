days = int(input())

years = int(days / 365)
days = days - (years * 365)
months = int(days / 30)
days = days - (months * 30)

print(str(years) + ' ano(s)')
print(str(months) + ' mes(es)')
print(str(days) + ' dia(s)')
