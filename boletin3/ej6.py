cadea1 = input('Introduzca a primeira cadea: ')
cadea2 = input('Introduzca a segunda cadea: ')
cadea3 = input('Introduzca a terceira cadea: ')

lonxitude_max = min([len(cadea1), len(cadea2), len(cadea3)])
prefixo_comun = ''
for i in range(0, lonxitude_max):
    if (cadea1[i] == cadea2[i] == cadea3[i]):
        prefixo_comun += cadea1[i]

if prefixo_comun == '':
    print('Non hai prefixo común')
else:
    print('O prefixo común mais largo é: ',prefixo_comun)