# Escribir un programa que pida al usuario un número entero e indique si es par o impar.

def par_impar(numero):
    modulo = numero % 2
    if modulo == 0:
        print(f"Su número {numero} es par.")
    else:
        print(f"Su número {numero} es impar.")

numero_ingresado = int(input("Ingrese un número entero: "))
par_impar(numero_ingresado)