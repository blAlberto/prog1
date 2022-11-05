#entrada de datos
cadena = input('Introduzca una cadena (los numeros pueden ser decimales con punto): ')

cadenas = cadena.split(' ')
n_numeros = 0

for palabra in cadenas: #Se procesa cada una de las palabras
    if (palabra == ''):
        continue # si hubese varios espacios seguidos el split produce cadenas vacias que no deben procesarse
    
    for caracter in palabra: #procesamos cada caracter de una palabra hasta que encontremos uno que no sea digito o punto
        if (not caracter.isdigit() and caracter != '.'): #se contemplan decimales con punto
            break
    
    n_numeros += 1

print('Hay {0} números en la cadena'.format(n_numeros))
