'''Escribir un programa que pida al usuario dos números enteros y 
muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son 
los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división
 entera respectivamente. '''
# Solicitar al usuario que ingrese dos números enteros
n = int(input("Por favor, ingrese el primer número entero (n): "))
m = int(input("Ahora, ingrese el segundo número entero (m): "))

# Calcular el cociente y el resto de la división entera
cociente = n // m
resto = n % m
divicion = n / m

# Mostrar el resultado por pantalla
print(f"{n} entre {m} da un cociente {cociente} y un resto {resto}")
print(f"{n} entre {m} da una divicion {divicion}")
