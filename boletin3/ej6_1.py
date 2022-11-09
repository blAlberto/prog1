# exercicio: 6.1
# autor: Alberto Bravo López
# email: alberto.bravo.lopez@rai.usc.es
# propósito: O programa recibirá tres cadeas e buscarase o máximo prefixo común entre as tres

print('Neste programa solicitaranse 3 cadeas por teclado e buscarase o máximo prefixo común entre as tres')

# Entrada de datos
cadea1 = input('Introduzca a primeira cadea: ')
cadea2 = input('Introduzca a segunda cadea: ')
cadea3 = input('Introduzca a terceira cadea: ')

# Procesado
lonxitude_max = min([len(cadea1), len(cadea2), len(cadea3)])
prefixo_comun = ''
for i in range(0, lonxitude_max):
    if (cadea1[i] == cadea2[i] == cadea3[i]):
        prefixo_comun += cadea1[i]
    else:
        break

if prefixo_comun == '':
    print('Non hai prefixo común')
else:
    print('O prefixo común mais largo é: ',prefixo_comun)