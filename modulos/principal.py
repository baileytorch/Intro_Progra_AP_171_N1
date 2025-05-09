import operaciones

def bienvenida():
    print()
    print("*** Super Calculadora Python ***")
    print("================================")
    
def menu():
    print()  
    print("Seleccione su Operación")
    print("1: Suma")
    print("2: Resta")
    print("3: Multiplicación")
    print("4: División")
    print("0: Salir")
    print()

def ejecutar_calculadora():
    bienvenida()  
    while True:
        print()
        num_1 = float(input("Ingrese Número 1: "))
        num_2 = float(input("Ingrese Número 2: "))
        menu()
        opcion = input("Seleccione su opción (0-4): ")
        
        resultado = 0
        operacion = ""
        
        if opcion == "1":
            resultado = operaciones.op_suma(num_1, num_2)
            operacion = "+"
        elif opcion == "2":
            resultado = operaciones.op_resta(num_1, num_2)
            operacion = "-"
        elif opcion == "3":
            resultado = operaciones.op_multiplicacion(num_1, num_2)
            operacion = "*"
        elif opcion == "4":
            resultado = operaciones.op_division(num_1, num_2)
            operacion = "/"
        elif opcion == "0":
            print("Saliendo del sistema... hacia otra galaxia...")
            break
        else:
            print("Opción Inválida... Vuelva a Ingresar...")
            return
        
        if resultado == None:
            print("Operación NO permitida...No se puede dividir por 0...")
        else:
            print(f"{num_1} {operacion} {num_2} = {resultado}")

ejecutar_calculadora()