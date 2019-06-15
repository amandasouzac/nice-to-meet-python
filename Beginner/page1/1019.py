ms = int(input())

h = int(ms / 3600)
ms = ms - (h * 3600)

m = int(ms / 60)
ms = ms - (m * 60)

print(str(h) + ':' + str(m) + ':' + str(ms))