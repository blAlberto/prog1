

cadea = input('Introduzca unha cadea: ')
lonx_subcadea = int(input('Introduzca a lonxitude das subcadeas a obter: '))

if lonx_subcadea > len(cadea):
    print('A lonxitude das subcadeas buscadas é superior á da cadea orixinal')
else:
    subcadeas = []
    for i in range(0, len(cadea) - lonx_subcadea + 1):
        subcadeas.append(cadea[i: i + lonx_subcadea])
    print('As subcadeas de lonxitude {} son {}'.format(lonx_subcadea, subcadeas))