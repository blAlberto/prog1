#entrada de datos
cadena = input('Introduzca una cadena (los numeros pueden ser decimales con punto): ')

cadenas = cadena.split(' ')
n_numeros = 0

for subcadena in cadenas: #Se procesa cada una de las palabras
    if (subcadena == ''):
        continue # si hubese varios espacios seguidos el split produce cadenas vacias que no deben procesarse
    es_numero = True
    for caracter in subcadena: #procesamos cada caracter de una palabra hasta que encontremos uno que no sea digito o punto
        if (not caracter.isdigit() and caracter != '.'): #se contemplan decimales con punto
            es_numero = False
            break
    if (es_numero):
        n_numeros += 1

print('Hay {0} números en la cadena'.format(n_numeros))
