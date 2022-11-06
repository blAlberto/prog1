n = int(input('Introduzca o número de primos que se obterán: '))

if (n < 1):
    print('Non hai números que obter')
    exit()

primos = [-1] * n
primos[0] = 1
primos_obtidos = 0
numero_actual = 1
while primos_obtidos < n:
    primo = True
    for i in range(2, numero_actual):
        #evitase o 1 e o propio número neste bucle para comprobar se hai algún divisor mais
        if numero_actual % i == 0:
            primo = False
            break
    if primo:
        primos[primos_obtidos] = numero_actual
        primos_obtidos += 1
    numero_actual += 1

print('A lista con {} números primos é {}'.format(n, primos))