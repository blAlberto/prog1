lista = [0, 1, 2, 3, 4, 5, 6,7, 8, 9]
print('Lista orixinal: ', lista)

#obtendo os elementos de indice impar con slices
print('Lista sen elmentos dos índices pares: ', lista[1::2])
#obtendo os elementos de indice impar cun bucle
lista_resultado = []
for i in range(0, len(lista)):
    if (i % 2 != 0):
        lista_resultado.append(lista[i])
print('Lista sen elmentos dos índices pares: ', lista_resultado)

#obtendo os elementos de valor impar con filter
lista_resultado = list(filter(lambda x: x % 2 != 0, lista))
print ('Lista cos elementos de valor impar: ', lista_resultado)

#obtendo os elentos de valor impar cun bucle
lista_resultado = []
for i in range(0, len(lista)):
    if (lista[i] % 2 != 0):
        lista_resultado.append(lista[i])
print('Lista cos elementos de valor impar: ', lista_resultado)
