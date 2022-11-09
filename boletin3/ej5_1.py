# exercicio: 5.1
# autor: Alberto Bravo López
# email: alberto.bravo.lopez@rai.usc.es
# propósito: O programa recibirá unha cadea e un número, e devolverá o número de subcadeas con esa lonxitude

print('Neste programa pedirase unha cadea por teclado e un número, e devolverase a lista de subcadeas con esa lonxitude')

# Entrada de datos
cadea = input('Introduzca unha cadea: ')
lonx_subcadea = int(input('Introduzca a lonxitude das subcadeas a obter: '))

# Procesado
if lonx_subcadea > len(cadea):
    print('A lonxitude das subcadeas buscadas é superior á da cadea orixinal')
else:
    subcadeas = []
    for i in range(0, len(cadea) - lonx_subcadea + 1):
        subcadeas.append(cadea[i: i + lonx_subcadea])
    print('As subcadeas de lonxitude {} son {}'.format(lonx_subcadea, subcadeas))