'''Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
Estos ahorros debido a intereses, que no se cobran hasta finales de año, 
se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad
 de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y
  mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años.
 Redondear cada cantidad a dos decimales.'''

monto = int(input("cantidad de dinero depositada en tu cuenta "))
interes = (4/100)


def calcular(mon, inters):
    cont = 1
    nomto1 = mon
    while cont < 4:
        # dos formas de imprimir
        print(f"el año {cont} tu balance final ma interes es {
              nomto1 + (nomto1 * inters)}")
        print("El año", cont, "tu balance final con intereses es",
              (nomto1 + (nomto1 * inters)))
        print("------------------------------------")
        nomto1 = nomto1 + (nomto1 * inters)
        cont += 1


calcular(monto, interes)
