def op_suma(a,b):
    return a + b

def op_resta(a,b):
    return a - b

def op_multiplicacion(a,b):
    return a * b

def op_division(a,b):
    if b == 0:
        print("El divisor de una división no puede ser 0.")
        return None
    else:
        return a / b