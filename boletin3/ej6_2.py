import sys

cadeas = []
cadea_leida = ''
lonx_cadea_pequena = sys.maxsize

cadea_leida = input('Introduzca cadea ("fin" para rematar): ')
while cadea_leida != 'fin':
    cadeas.append(cadea_leida)
    lonx_cadea_pequena = min(lonx_cadea_pequena, len(cadea_leida))
    cadea_leida = input('Introduzca cadea ("fin" para rematar): ')

if(len(cadeas) == 0):
    print('Non hai cadeas')
elif (len(cadeas) == 1):
    print('O prefixo común é "{}"'.format(cadeas[0]))
else:
    pos_max_comun = 0
    i_caracter = 0
    mismatch = False
    while not mismatch and i_caracter < lonx_cadea_pequena:
        #iterador sobre as posicions de cada cadea
        for i_cadea in range(1, len(cadeas)):
            #iteramos desde a segunda cadea da lista para comparar o caracter actual co da cadea anterior na lista
            if cadeas[i_cadea][i_caracter] != cadeas[i_cadea - 1][i_caracter]:
                mismatch = True
                break
        if not mismatch:
            pos_max_comun += 1        
            i_caracter +=1
    print('O máximo prefixo común é "{}"'.format(cadeas[0][0:pos_max_comun]))
