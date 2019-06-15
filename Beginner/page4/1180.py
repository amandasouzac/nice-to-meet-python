N = int(input())
vector = list(map(int, input().split()))

smallest = min(vector)
pos = vector.index(smallest)
print('Menor valor: %d' % (smallest))
print('Posicao: %d' % (pos))