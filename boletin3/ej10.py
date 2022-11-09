# exercicio: 10
# autor: Alberto Bravo López
# email: alberto.bravo.lopez@rai.usc.es
# propósito: O programa inicializa unha lista da que despois:
#   - obteranse os elementos de índice impar
#   - obteranse os elementos de valor par

print('Neste programa, a partir dunha lista xa creada, eliminaranse os elementos de indice par, e despois os elementos de valor par')
lista = [0, 1, 2, 3, 4, 5, 6,7, 8, 9]
print('Lista orixinal: ', lista)

#obtendo os elementos de indice impar con slices
print('Lista sen elmentos dos índices pares con slices: ', lista[1::2])
#obtendo os elementos de indice impar cun bucle
lista_resultado = []
for i in range(0, len(lista)):
    if (i % 2 != 0):
        lista_resultado.append(lista[i])
print('Lista sen elmentos dos índices pares con bucle: ', lista_resultado)

#obtendo os elementos de valor impar con filter
lista_resultado = list(filter(lambda x: x % 2 != 0, lista))
print ('Lista cos elementos de valor impar con filter: ', lista_resultado)

#obtendo os elentos de valor impar cun bucle
lista_resultado = []
for i in range(0, len(lista)):
    if (lista[i] % 2 != 0):
        lista_resultado.append(lista[i])
print('Lista cos elementos de valor impar con bucle: ', lista_resultado)
