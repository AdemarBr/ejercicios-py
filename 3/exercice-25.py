'''Escribir un programa que pida al usuario que introduzca una 
frase en la consola y muestre por pantalla la frase invertida.'''
frase = input("ingresa una frase ")

def inversa(f):
    res = ""
    for charr in f:
        res = charr + res
    return res


print( inversa(frase))