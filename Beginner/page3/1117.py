score1 = -1
score2 = -1

invalid = 0

while (score1 < 0 or score2 < 0):
    s = float(input())

    if s >= 0 and s <= 10:
        if score1 < 0:
            score1 = s
        else:
            score2 = s
    else:
        invalid += 1
        
for i in range(0, invalid):
    print('nota invalida')

media = (score1 + score2)/2
print('media = ' + '%.2f' % media)