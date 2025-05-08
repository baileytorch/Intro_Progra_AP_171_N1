
from itertools import cycle

# # Definición de funciones

# # Ejercicio 1
def saludar(nombre):
    return f"Hola admirable {nombre}"

# # Llamar a una función
# print()
# nombre = input("Ingrese su nombre: ")
# saludar(nombre)

# # Ejercicio 2
def sumar(a,b):
    resultado = a + b
    return resultado

# print()
# sumar(5,7)

# # Ejercicio 3
# num_1 = int(input("Ingrese el primer valor: "))
# num_2 = int(input("Ingrese el segundo valor: "))

# print()
# sumar(num_1,num_2)

# Ejercicio 4
def operar(a,b,op):
    resultado = 0
    if op == "+":
        resultado = a + b
    elif op == "-":
        resultado = a - b
    elif op == "*":
        resultado = a * b
    elif op == "/":
        if b != 0:
            resultado = a / b
        else:
            print("El divisor de una división no puede ser 0.")
            return
    else:
        print("Operación incorrecta...")
    return f"{a}{op}{b} = {resultado}"

def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11