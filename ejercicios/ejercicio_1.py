# Escribir un programa que almacene la cadena de caracteres 'CONTRASENA' en una variable. 
# Luego le pida al usuario que ingrese la contraseña y el sistema debe indicar por pantalla 
# si la contraseña ingresada es correcta

def validacion_contrasena(contrasena_usuario):
    contrasena = "Todos_juntos"
    if contrasena_usuario == contrasena:
        print("Contraseña Correcta.")
    else:
        print("Contraseña Incorrecta.")

contrasena_ingresada = input("Ingrese su contraseña: ")
validacion_contrasena(contrasena_ingresada)