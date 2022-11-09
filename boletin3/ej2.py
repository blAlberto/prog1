# exercicio: 2
# autor: Alberto Bravo López
# email: alberto.bravo.lopez@rai.usc.es
# propósito: comprobar se un texto esta ben parentizado.


# def de funcions para diferentes casos 
def ben_parentizado_simple(cadena):
# comprobarase que se peche cada parentesis antes de abrir outro (non contempla anidamento)
    parentesis_aberto = False
    for caracter in cadena:
        if (caracter == '(' and parentesis_aberto):
            return False
        elif (caracter == '(' and not parentesis_aberto):
            parentesis_aberto = True
        elif (caracter == ')' and parentesis_aberto):
            parentesis_aberto = False
        elif (caracter == ')' and not parentesis_aberto):
            return False

    return True


def bien_parentizado_anidado(cadena):
# valida cadeas con parentesis abertos antes de pechar outros
    parentesis_abertos = 0
    for caracter in cadena:
        if (caracter == '('):
            #ao contemplarse o anidameento os parentesis abertos engadense sen problema
            parentesis_abertos += 1
        elif (caracter == ')' and parentesis_abertos == 0):
            #se hai un parentesis de peche y non hai ningun aberto pendiente, non esta ben parentizado
            parentesis_abertos = False
        elif (caracter == ')' and parentesis_abertos > 0):
            #ao pechar un parentesis este eliminase dos pendientes
            parentesis_abertos -= 1
    #se se terminou de procesar a cadea o resultado dependera de se quedaron parentesis abertos
    return parentesis_abertos == 0


def ben_parentizado_multiple(cadena):
#contemplase anidamiento de parentesis, corchetes y chaves
    signos_apertura = ['(', '[', '{']
    signos_cierre = [')', ']', '}']
    signos_apertura_cadena = [] #sera unha pila onde se garden os signos de apertura
    for caracter in cadena:
        if (caracter in signos_apertura):
            signos_apertura_cadena.append(caracter)
        if (caracter in signos_cierre):
            ultimo = signos_apertura_cadena.pop()
            #se no coincide o signo que pecha co ultimo que esta aberto na pila non estara ben parentizado
            if (signos_apertura.index(ultimo) != signos_cierre.index(caracter)):
               return False 

    return True

print('Neste programa pedirase un texto e comprobarase se está ben parentizado')
# entrada de datos
cadena = input('Introduzca un texto: ')

# procesado
print('Parentizado simple: ' + ('OK ' if ben_parentizado_simple(cadena) else 'KO'))

print('Parentizado anidado: ' + ('OK ' if bien_parentizado_anidado(cadena) else 'KO'))

print('Parentizado incluindo chaves e corchetes anidados: ' + ('OK ' if ben_parentizado_multiple(cadena) else 'KO'))