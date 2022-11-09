# exercicio: 6.2
# autor: Alberto Bravo López
# email: alberto.bravo.lopez@rai.usc.es
# propósito: O programa recibirá Cadeas por teclado e devolvera o máximo prefixo común

import sys

cadeas = []
cadea_leida = ''
#obteño o tamaño maximo dunha cadea para que calquera introducida sexa menor
lonx_cadea_pequena = sys.maxsize 

print('Neste programa solicitaranse cadeas por teclado ata teclear "fin", e devolverase o máximo prefixo común de todas elas')

# Entrada de datos
cadea_leida = input('Introduzca cadea ("fin" para rematar): ')
while cadea_leida != 'fin':
    cadeas.append(cadea_leida)
    lonx_cadea_pequena = min(lonx_cadea_pequena, len(cadea_leida))
    cadea_leida = input('Introduzca cadea ("fin" para rematar): ')

# Procesado

# comprobo un par de casos base, se non hai cadeas e se solo hai unha xa que o resultado e directo nestes casos
if(len(cadeas) == 0):
    print('Non hai cadeas')
elif (len(cadeas) == 1):
    print('O prefixo común é "{}"'.format(cadeas[0]))
else:
    pos_max_comun = 0
    i_caracter = 0
    mismatch = False
    while not mismatch and i_caracter < lonx_cadea_pequena:
        #itera sobre cada posicion das cadeas mentres haxa coincidencias en todas elas
        for i_cadea in range(1, len(cadeas)):
            #iteramos desde a segunda cadea da lista para comparar o caracter actual co da cadea anterior na lista
            if cadeas[i_cadea][i_caracter] != cadeas[i_cadea - 1][i_caracter]:
                #se non hai coincidencia rompe o bucle e quedamos co indice actual que sirve para facer 
                #o slice xa que está unha posicion por diante do prefixo máximo común
                mismatch = True
                break
             
        if not mismatch:
            #se todo vai ben incrementamos os contadores
            pos_max_comun += 1        
            i_caracter +=1
            
    print('O máximo prefixo común é "{}"'.format(cadeas[0][0:pos_max_comun]))
