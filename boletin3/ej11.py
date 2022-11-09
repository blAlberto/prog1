# exercicio: 11
# autor: Alberto Bravo López
# email: alberto.bravo.lopez@rai.usc.es
# propósito: O programa solicita un número para crear unha matriz identidade con esa dimension

print('Neste progrmaa solicitarase un número para crear unha matriz identidade desa dimensión')

# Entrada de datos
n = int(input('Introduzca un entero positivo (sera el ancho y alto de la matriz): '))

# Procesado
if (n < 0 ):
    #utilizo o exit como se fose o return dun método e evito un nivel de indentación no resto do programa
    exit() 

# Inicializo a matriz con todos os valores a 0 para despois iterar facilmente e poñer a 1 a diagonal
M = [[0] * n for i in range(0, n)] 

for i in range(0, n):
    M[i][i] = 1

print('La matriz identidad de dimension', n, 'es', M)