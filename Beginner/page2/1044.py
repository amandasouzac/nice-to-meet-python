values = list(map(int, input().split()))
values.sort()

if values[1] % values[0] == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')