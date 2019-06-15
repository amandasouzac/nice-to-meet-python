values = input().split()
X = int(values[0])
Y = int(values[1])
Z = int(values[2])

def MaiorAB(A, B):
    return (A + B + abs(A-B))/2

maior = int(MaiorAB(X, MaiorAB(Y, Z)))
print(str(maior) + ' eh o maior')