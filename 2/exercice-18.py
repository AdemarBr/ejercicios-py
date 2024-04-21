'''Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete 
así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos 
en el último pedido y calcule el peso total del paquete que será enviado.'''


numPayasos = int(input("ingrese la cantidad de payasos en el ultimo pedido "))
numMuñecas = int(input("ingrese la cantidad de muñecas en el ultimo pedido "))
pM = 75
pP = 112


def pesoTotal(m, p):
    return ((m * pM) + (p * pP))


print("peso total del envio es", pesoTotal(numMuñecas, numPayasos), "Gr")
print(f"peso total del envio es {pesoTotal(numMuñecas, numPayasos)} gr")
