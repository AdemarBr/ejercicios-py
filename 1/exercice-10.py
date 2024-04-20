'''Definir un histograma procedimiento() que tome una lista de números enteros e imprima un
histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
****
*********
******* '''
lista1 = [4, 9, 7]


def procedimiento(lista):
    for l in lista:
        print(l * "*")


procedimiento(lista1)
