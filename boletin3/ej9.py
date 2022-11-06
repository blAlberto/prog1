enteros = [-1] * 10
actual = 0

while actual < 10:
    num = int(input('Introduzca número positivo, se non o é pedirase de novo: '))
    while num < 0:
        num = int(input('O número non e positivo, probe de novo: '))
    enteros[actual] = num
    actual += 1

print('Os números introducidos son ', enteros)