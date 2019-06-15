values = list(map(int, input().split()))

start_hour = values[0]
start_minute = values[1]
finish_hour = values[2]
finish_minute = values[3]

hours_duration = (24 - start_hour) + finish_hour

if hours_duration > 24:
    hours_duration -= 24

minutes_duration = finish_minute - start_minute

if minutes_duration < 0:
    hours_duration -= 1
    minutes_duration += 60
elif minutes_duration > 0 and start_hour == finish_hour:
    hours_duration = 0



print('O JOGO DUROU ' + str(hours_duration) + ' HORA(S) E '+ str(minutes_duration) +' MINUTO(S)')