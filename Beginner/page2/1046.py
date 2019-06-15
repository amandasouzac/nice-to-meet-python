hours = list(map(int, input().split()))
start = hours[0]
finish = hours[1]

duration = (24 - start) + finish

if duration > 24:
    duration -= 24

print('O JOGO DUROU '+ str(duration) +' HORA(S)')