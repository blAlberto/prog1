# exercicio: 1
# autor: Alberto Bravo López
# email: alberto.bravo.lopez@rai.usc.es
# propósito: mostrar a cantidade de números nunha cadea (non solo díxitos)

print('Neste programa pedirase unha cadea por teclado e devolverase o número de números(non solo díxitos e aceptando decimais) presentes na mesma')
#entrada de datos
cadena = input('Introduza unha cadea: ')

cadenas = cadena.split(' ')
n_numeros = 0

for palabra in cadenas: 
    # procénsanse as palabras
    if (palabra == ''):
        # se hai varios espacios seguidos o split devolverá unha cadea vacia, deste xeito evitase
        continue 
    
    for caracter in palabra: 
        # procesamos cada caracter dunha palabra ata que encontremos un que non sexa dixito ou punto para contemplar decimais
        if (not caracter.isdigit() and caracter != '.'): 
            break
    
    n_numeros += 1

print('Hay {0} números en la cadena'.format(n_numeros))
