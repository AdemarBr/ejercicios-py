'''Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
Después debe mostrar por pantalla la paga que le corresponde.'''

horas = input("cuantas horas trabajas  :")
pago = input("cuanto te pagan por hora  :")

print("la paga que te corresponde es ", int(horas) * int(pago))
