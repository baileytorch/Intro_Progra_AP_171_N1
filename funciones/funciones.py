# Definición de funciones

# Ejercicio 1
def saludar(nombre):
    print(f"Hola admirable {nombre}")

# Llamar a una función
print()
nombre = input("Ingrese su nombre: ")
saludar(nombre)

# Ejercicio 2
def sumar(a,b):
    resultado = a + b
    print(resultado)

print()
sumar(5,7)

# Ejercicio 3
num_1 = int(input("Ingrese el primer valor: "))
num_2 = int(input("Ingrese el segundo valor: "))

print()
sumar(num_1,num_2)

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
    print(f"{a}{op}{b} = {resultado}")
    
respuesta = "SI"
while True:
    if respuesta.upper() == "SI":    
        numero_1 = int(input("Ingrese el primer valor: "))
        numero_2 = int(input("Ingrese el segundo valor: "))
        operacion = input("Ingrese la operación a realizar: ")        

        operar(numero_1, numero_2, operacion)
        respuesta = input("¿'Desea realizar una operación? Responda SI o NO ")
    else:
        break
    
