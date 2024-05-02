'''Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
 y después muestre por pantalla
 la misma frase pero con la vocal introducida en mayúscula'''

frase = input("intrdoduce una frase: ")
vocal =input("introduce una vocal: ")

res = ""
for l in frase:
    if l == vocal:
        res = res + l.upper()
    else:
        res = res + l

print(res)



print("con funcion nativa de python ")
print(frase.replace(vocal, vocal.upper()))