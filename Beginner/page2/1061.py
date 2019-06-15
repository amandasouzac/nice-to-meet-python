ds = int(input().split()[1])
start = input().split()
hs = int(start[0])
ms = int(start[2])
ss = int(start[4])

df = int(input().split()[1])
finish = input().split()
hf = int(finish[0])
mf = int(finish[2])
sf = int(finish[4])

days_duration = df - ds

hours_duration = hf - hs
if hours_duration < 0:
    days_duration -= 1
    hours_duration += 24
elif hours_duration > 0 and df == ds:
    days_duration = 0

minutes_duration = mf - ms
if minutes_duration < 0:
    hours_duration -= 1
    minutes_duration += 60
elif minutes_duration > 0 and hs == hf:
    hours_duration = 0

seconds_duration = sf - ss
if seconds_duration < 0:
    minutes_duration -= 1
    seconds_duration += 60
elif seconds_duration > 0 and ms == mf:
    minutes_duration = 0

print(str(days_duration) + ' dia(s)')
print(str(hours_duration) + ' hora(s)')
print(str(minutes_duration) + ' minuto(s)')
print(str(seconds_duration) + ' segundo(s)')