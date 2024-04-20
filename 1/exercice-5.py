'''Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente
todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4])
debería devolver 24.'''
lista1 = [1, 2, 3, 4]


def suma(lista):
    resul = 0
    for num in lista:
        resul += num
    return resul


def multi(lista):
    resul = 1
    for num in lista:
        resul *= num
    return resul


print("suma = ", suma(lista1))
print("multiplicacion = ", multi(lista1))
