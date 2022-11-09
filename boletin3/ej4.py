# exercicio: 4
# autor: Alberto Bravo López
# email: alberto.bravo.lopez@rai.usc.es
# propósito: O programa recibirá unha cadea e un número, e devolverá unha cadea da mesma lonxitude con
#   cada carácter desplazado tantas posicións a dereita no abecedario como indique o número introducido


#---- Funcions ------
# Declaro un par de funcións para facer mais lexible o bloque de procesado
# A mesma función de codificar servirá tamen para decodificar, pasando o desplazamento como un número negativo

def desplaza_n_posicions(lista, indice, desplazamento):
# funcion que colle unha lista, un caracter da mesma e devolve o resultante de desplazarse n posicions
    return lista[(lista.index(indice) + desplazamento) % len(lista)]

def codifica_cadea(cadea, desplazamento):
# funcion que codifica a cadea en base ao desplazamento
    cadena_codificada = ''
    for caracter in cadea:
        if caracter.isalpha() and caracter.islower():
            cadena_codificada += desplaza_n_posicions(minusculas, caracter, desplazamento)
        elif caracter.isalpha() and caracter.isupper():
            cadena_codificada += desplaza_n_posicions(mayusculas, caracter, desplazamento)
        elif (caracter.isdigit()):
            cadena_codificada += str((int(caracter) + desplazamento)%10)
        else:
            cadena_codificada += caracter
    return cadena_codificada

# Para realizar os desplazamentos utilizarei listas que conteñan as letras e os números para moverme mediante
# indices e modulos
minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


print('Neste programa pedirase unha cadea e un número que será o desplazamento que lle apliquemos para codificala')
print('A continuación pedirase outra cadea e o desplazamento que se lle aplicou para decodificala')
#-Codificacion-
# Entrada de datos
cadea = input('Introduzca unha cadea para codificar: ')
desplazamento = int(input('Introduzca o desplazamento a aplicar: '))

# Procesado
print('A cadea codificada e: ', codifica_cadea(cadea, desplazamento))

#-Decodificacion-
# Entrada de datos
cadea = input('Introduzca unha cadea para decodificar: ')
desplazamento = int(input('Introduzca o desplazamento que se lle aplicou: '))

print('A cadea orixinal era: ', codifica_cadea(cadea, -desplazamento))