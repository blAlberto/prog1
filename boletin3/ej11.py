
n = int(input('Introduzca un entero positivo (sera el ancho y alto de la matriz): '))
if (n < 0 ):
    #utilizo o exit como se fose o return dun método e evito un nivel de indentación no resto do programa
    exit() 

M = [[0] * n for i in range(0, n)]

for i in range(0, n):
    M[i][i] = 1

print('La matriz identidad de dimension', n, 'es', M)