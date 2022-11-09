# exercicio: 8
# autor: Alberto Bravo López
# email: alberto.bravo.lopez@rai.usc.es
# propósito: O programa recibirá un número e devolerá esa cantidade de números primos desde o 1

print('Neste progrma solicitarase un número e devolveranse tantos números primos')

# Entrada de datos
n = int(input('Introduzca o número de primos que se obterán: '))

# Procesado

# Valido que o número sexa positivo. Se non o é, a partir deste exercicio, utilizo exit() para deter o programa
# cun comportamento similar ao return dun método, e así evito o nivel extra de indentación no resto do programa
if (n < 1):
    print('Non hai números que obter')
    exit()

primos = []
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
        primos.append(numero_actual)
        primos_obtidos += 1
    numero_actual += 1

print('A lista con {} números primos é {}'.format(n, primos))