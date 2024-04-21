'''Una panadería vende barras de pan a 3.49€ cada una. 
El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience
 leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar 
 el precio habitual de una barra de pan,
 el descuento que se le hace por no ser fresca y el coste final total.'''

precioDia = 3.49
precioDescuento = precioDia - (precioDia * (60/100))

num = int(input("numero de barrar vendidad no frescas "))
print(f"precio unitario habitual {precioDia}")
print(f"precio habitual {precioDia * num}")
print(f"descuento {num * precioDia * 0.6}")
print(f"costo total {num * precioDescuento}")
print(" --------------------------------------------------------")


# Precio habitual de una barra de pan
precio_habitual = 3.49

# Solicitar al usuario el número de barras vendidas que no son del día
barras_no_frescas = int(
    input("Ingrese el número de barras vendidas que no son del día: "))

# Calcular el descuento y el costo final total
descuento = barras_no_frescas * precio_habitual * 0.60
costo_final_total = barras_no_frescas * precio_habitual * 0.40

# Mostrar el precio habitual de una barra de pan, el descuento y el costo final total
print("Precio habitual de una barra de pan:", precio_habitual, "€")
print("Descuento por no ser fresca:", descuento, "€")
print("Costo final total:", costo_final_total, "€")
