# exercicio: 9
# autor: Alberto Bravo López
# email: alberto.bravo.lopez@rai.usc.es
# propósito: O programa pedirá 10 enteiros por teclado, validará que son positivos e volverá pedilos se non o son


# neste exercicio inicializo a lista coas 10 posicions como se fose un array nas que irei asignando os 
# valores a medida que os reciba  en lugar de crear a lista vacia e ir engadindoos
enteros = [-1] * 10
actual = 0

print('Neste programa pediranse 10 números positivos, se se introduce un negativo pedirase de novo')
while actual < 10:
    num = int(input('Introduzca número positivo, se non o é pedirase de novo: '))
    while num < 0:
        num = int(input('O número non e positivo, probe de novo: '))
    enteros[actual] = num
    actual += 1

print('Os números introducidos son ', enteros)