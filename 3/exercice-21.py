'''Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e 
imprima por pantalla en líneas distintas el nombre del usuario tantas veces como 
el número introducido.'''

nombre = input("ingresa tu nombre ")
num = int(input("ingresa un numero "))

cont = 1
while cont <= num:
    print(nombre)
    cont += 1
