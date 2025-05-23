from operaciones import op_suma, op_resta, op_multiplicacion, op_division

def menu():
    print("Seleccione su Opción")
    print("[1] Realizar un Cálculo Aritmético")
    print("[2] salir de Sistema")

def programa_principal():
    print("Super calculadora en Python")
    print("===========================")

    while True:
        menu()
        opcion_menu = input("Seleccione 1 o 2: ")

        if opcion_menu == "1":
            numero_1 = float(input("Ingrese el primer valor: "))
            numero_2 = float(input("Ingrese el segundo valor: "))
            operacion = input("Ingrese la operación a realizar: ")
            resultado = 0       

            if operacion == "+":
                resultado = op_suma(numero_1,numero_2)

            elif operacion == "-":
                resultado = op_resta(numero_1,numero_2)

            elif operacion == "*":
                resultado = op_multiplicacion(numero_1,numero_2)
            
            elif operacion == "/":
                resultado = op_division(numero_1,numero_2)
            else:
                print("Operación Inválida...")
            
            if resultado == None:            
                print("El divisor de una división no puede ser 0.")
            else:
                print()
                print(f"{numero_1} {operacion} {numero_2} = {resultado}")        
        else:
            break

programa_principal()
