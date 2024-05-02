'''Escribir un programa que pregunte por consola por los productos de una cesta de la compra,
 separados por comas, y muestre por pantalla
 cada uno de los productos en una línea distinta.'''
 


Productos = input("ingresa los productos de tu sesta separados por coma :  ")

def verLista(p):
    listaP = p.split(",")
    for p in listaP:
      print(p)

verLista(Productos)