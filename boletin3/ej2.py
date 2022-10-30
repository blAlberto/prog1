# def de funciones
def bien_parentizado_simple(cadena):
#se comprobara que se cierre cada parentesis antes de abrir otro (no contempla anidamiento)
    parentesis_abierto = False
    for caracter in cadena:
        if (caracter == '(' and parentesis_abierto):
            return False
        elif (caracter == '(' and not parentesis_abierto):
            parentesis_abierto = True
        elif (caracter == ')' and parentesis_abierto):
            parentesis_abierto = False
        elif (caracter == ')' and not parentesis_abierto):
            return False

    return True

def bien_parentizado_anidado(cadena):
#se contempla anidamiento de parentesis, corchetes y llaves
    signos_apertura = ['(', '[', '{']
    signos_cierre = [')', ']', '}']
    signos_apertura_cadena = [] #sera unha pila onde se garden os signos de apertura
    for caracter in cadena:
        if (caracter in signos_apertura):
            signos_apertura_cadena.append(caracter)
        if (caracter in signos_cierre):
            ultimo = signos_apertura_cadena.pop()
            #si no coincide el que cierra con el ultimo que esta abierto en la pila no estara bien parentizado
            if (signos_apertura.index(ultimo) != signos_cierre.index(caracter)):
               return False 

    return True


# entrada de datos
cadena = input('Introduzca un texto, se validara si está bien parentizado: ')

# procesado
print('El texto ' + ('está ' if bien_parentizado_simple(cadena) else 'no está ') + 'bien parentizado')

print('El texto ' + ('está ' if bien_parentizado_anidado(cadena) else 'no está ') + 'bien parentizado')

