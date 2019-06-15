par = []
impar = []

def printArray(a, name):
    for i in range(0, len(a)):
        print('%s[%d] = %d' % (name, i, a[i]))

for i in range(15):
    x = int(input())
    if x%2 == 0:
        if len(par) == 5:
            printArray(par, 'par')
            par = []

        par.append(x)
    else:
        if len(impar) == 5:
            printArray(impar, 'impar')
            impar = []

        impar.append(x)
    
printArray(impar, 'impar')
printArray(par, 'par')
