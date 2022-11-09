# exercicio: 3
# autor: Alberto Bravo López
# email: alberto.bravo.lopez@rai.usc.es
# propósito: comprobar se unha cadea de texto introducida por teclado e un palindromo

#entrada de datos 
cadena = input('Introduza unha cadea para comprobar se é palíndromo: ')

letras = ''
#obtemos unha cadea con solo as letras en minuscula
for caracter in cadena:
    if caracter.isalpha():
        letras += caracter.lower()

palindromo = True
#recorremos a cadea desde os extremos cara o centro comprobando que os caracteres son iguales
#se nalgun punto falla, a frase non sera un palindromo
for i in range(0, len(letras)//2):
    if letras[i] != letras [-(i+1)]:
        palindromo = False
        break
print('A frase é palíndromo' if palindromo else 'A frase non é palíndromo')