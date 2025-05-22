from operaciones import op_suma, op_resta, op_multiplicacion, op_division

respuesta = "SI"
while True:
    if respuesta.upper() == "SI":    
        numero_1 = float(input("Ingrese el primer valor: "))
        numero_2 = float(input("Ingrese el segundo valor: "))
        operacion = input("Ingrese la operación a realizar: ")        

        if operacion == "+":
            resultado = op_suma(numero_1,numero_2)
    else:
        break
