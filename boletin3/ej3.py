#entrada de datos 
cadena = input('Introduzca una cadena para comprobar si es palindromo: ')

letras = ''
#obtenemos una cadena con solo las letras en minuscula
for caracter in cadena:
    if caracter.isalpha():
        letras += caracter.lower()

palindromo = True
#recorremos la cadena desde los extremos hacia el centro comprobando que los caracteres son iguales
#si en algun punto falla, la frase no sera un palindormo
for i in range(0, len(letras)//2):
    if letras[i] != letras [-(i+1)]:
        palindromo = False
        break
print('La frase es palíndromo' if palindromo else 'La frase no es palíndromo')