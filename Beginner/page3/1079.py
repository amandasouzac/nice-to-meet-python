N = int(input())
averages = []

for i in range(0, N):
    values = list(map(float, input().split()))
    average = ((values[0] * 2) + (values[1] * 3) + (values[2] * 5)) / 10
    averages.append(average)

for a in averages:
    print('%.1f' % a)
