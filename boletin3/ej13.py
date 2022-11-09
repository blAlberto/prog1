# exercicio: 13
# autor: Alberto Bravo López
# email: alberto.bravo.lopez@rai.usc.es
# propósito: O programa xerará unha matriz aleatoriamente, calculará a suma de cada fila e columna, 
# e comprobará se coincide con outra

from random import randint

# Xeración aleatoria da matriz
filas = randint(1, 5)
columnas = randint(1, 5)

matriz = [[0] * columnas for i in range (0, filas)]

for fila in range(0, filas):
    for col in range(0, columnas):
        matriz[fila][col] = randint(0, 5)

print('Neste programa, a partir dunha matriz xerada aleatoriamente, comprobarase se a suma dos elementos',
 'dalgunha fila e igual á suma dos elementos dalgunha columna')

print('A matriz de ', filas, 'x', columnas,' creada é :', matriz)

# Cálculo das sumas de filas e columnas
sumaFilas = [0] * filas
sumaCols = [0] * columnas

for fila in range(0, filas):
    for col in range(0, columnas):
        sumaFilas[fila] += matriz[fila][col]
        sumaCols[col] += matriz[fila][col]

print('A suma de cada fila é ', sumaFilas)
print('A suma de cada columna é ', sumaCols)

comuns = set()
# creo un set para poder amosar os elementos comun por consola e evitar os elementos repetidos
for item in sumaFilas:
    if(item in sumaCols):
        comuns.add(item)

if len(comuns) > 0:
    print('Hai filas e columnas coas mesmas sumas:',comuns)
else:
    print('Non hai ningunha fila que teña a mesma suma que unha columna')