
#Extraense 2 funcións xa que o código estaba sendo repetido é resulta mais lexible no caso de obter o caracter desplazado
# e porque decodificar é o mesmo que codificar co desplazamento negativo

#---- Funcions ------
#funcion que colle unha lista, un caracter da mesma e devolve o resultante de desplazarse n posicions
def desplaza_n_posicions(lista, indice, desplazamento):
    return lista[(lista.index(indice) + desplazamento) % len(lista)]
#funcion que codifica a cadea en base ao desplazamento
def codifica_cadea(cadea, desplazamento):
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

#listas cos 3 tipos de caracteres que usaremos
minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Entrada de datos
cadea = input('Introduzca unha cadea para codificar: ')
desplazamento = int(input('Introduzca o desplazamento a aplicar: '))

# Procesado
print('A cadea codificada e: ', codifica_cadea(cadea, desplazamento))

cadea = input('Introduzca unha cadea para decodificar: ')
desplazamento = int(input('Introduzca o desplazamento que se lle aplicou: '))

print('A cadea orixinal era: ', codifica_cadea(cadea, -desplazamento))