
dimension = list(map(lambda item: int(item), input('Introduzca enteiros para as dimensions da matriz co formato "m,n": ').split(',')))

if (len(dimension) != 2):
    exit('O formato non e correcto')

matriz = [[0] * dimension[1] for i in range(0, dimension[0])]

for n in range(0, dimension[0]):
    for m in range(0, dimension[1]):
        matriz[n][m] = int(input('Elemento [{},{}]: '.format(n, m)))

print(matriz)

vector_resultado = []
for n in range(0, dimension[1]):
    acumulador = 0
    for m in range(0, dimension[0]):
        acumulador += matriz[m][n]
    vector_resultado.append(acumulador)

print('O vector resultado de sumar os elementos de cada columna é: ', vector_resultado)