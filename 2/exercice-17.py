'''Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla 
el capital obtenido en la inversión.'''

# Solicitar al usuario la cantidad a invertir, el interés anual y el número de años
cantidad_invertir = float(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interés anual (%): "))
num_anios = int(input("Ingrese el número de años: "))

# Calcular el capital obtenido en la inversión
capital_obtenido = cantidad_invertir * (1 + interes_anual / 100) ** num_anios

# Mostrar el capital obtenido por pantalla
print("El capital obtenido en la inversión es:", capital_obtenido)
