# exercicio: 12
# autor: Alberto Bravo López
# email: alberto.bravo.lopez@rai.usc.es
# propósito: O programa pedirá as dimensións dunha matriz e despois os valores de cada posición para obter un vector
#    que teña como componentes a suma dos valores de cada columna

# Entrada de datos

print('Neste programa pediranse as dimensións dunha matriz e os seus valores para obter un vector que teña como compoñentes a suma dos valores de cada columna da matriz')

filas = int(input('Introduzca o número de filas: '))
columnas = int(input('Introduzca o número de columnas: '))


if (filas < 1 or columnas < 1):
    exit('As dimensións non son correctas')

matriz = [[0] * columnas for i in range(0, filas)]

for n in range(0, filas):
    for m in range(0, columnas):
        matriz[n][m] = int(input('Elemento [{},{}]: '.format(n, m)))

print(matriz)

vector_resultado = []
for n in range(0, columnas):
    acumulador = 0
    for m in range(0, filas):
        acumulador += matriz[m][n]
    vector_resultado.append(acumulador)

print('O vector resultado de sumar os elementos de cada columna é: ', vector_resultado)