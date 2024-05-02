'''Escribir un programa que pregunte por consola el precio de un
 producto en euros con dos decimales y muestre por pantalla el número de euros y 
el número de céntimos del precio introducido.'''
dato = (input("intrude el preco de un producto en euros con 2 decmales "))


print(int(float(dato)), "Euros con ", dato[-2:], "centimos" )

