

cadea = input('Introduzca unha cadea: ')
subcadea = input('Introduzca a cadea a buscar na anterior: ')

if (len(subcadea) > len(cadea)):
    print('A cadea buscada non está na primeira xa que a súa lonxitude e maior')
else:
    cadea_atopada = False
    for i in range(0, len(cadea) - len(subcadea) + 1):
        if (subcadea == cadea[i: i + len(subcadea)]):
            print('A cadea buscada está presente')
            cadea_atopada = True
            break
    if (not cadea_atopada):
        print('A cadea non está presente')