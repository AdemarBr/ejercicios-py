'''Escribir un programa que pregunte al usuario la fecha de su 
nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
 Adaptar el programa anterior para que también funcione cuando
 el día o el mes se introduzcan con un solo carácter.'''

def obtener_fecha():
    fecha = input("Ingrese su fecha de nacimiento en formato dd/mm/aaaa: ")
    # Dividir la fecha en día, mes y año
    partes_fecha = fecha.split('/')
    
    # Manejar días y meses con un solo carácter
    dia = partes_fecha[0].zfill(2)  # Rellenar con ceros a la izquierda si es necesario
    mes = partes_fecha[1].zfill(2)  # Rellenar con ceros a la izquierda si es necesario
    año = partes_fecha[2]
    
    return dia, mes, año

def mostrar_fecha(dia, mes, año):
    print("Día:", dia)
    print("Mes:", mes)
    print("Año:", año)

if __name__ == "__main__":
    dia, mes, año = obtener_fecha()
    mostrar_fecha(dia, mes, año)

