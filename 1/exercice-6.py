'''Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena
"estoy probando" debería devolver la cadena "odnaborp yotse"'''


def inversa(cadena):
    res = ""
    for charr in cadena:
        res = charr + res
    return res


cade = "briyan"

print("la inversa es: ", inversa(cade))
