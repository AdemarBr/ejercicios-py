'''Escribir un programa que pregunte el correo electrónico del usuario en la consola y 
muestre por pantalla otro correo electrónico con el mismo nombre 
(la parte delante de la arroba @) pero con dominio ceu.es.'''


correo = input("ingresa un correo electtronico: ")

def cambCorreo(email):
    r =""
    for ch in email:
        if ch != "@":
            r = r + ch
        else:
            return r+"@ceu.es"

print(cambCorreo(correo))