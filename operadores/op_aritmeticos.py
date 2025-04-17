# Operadores aritméticos, permiten realizar operaciones entre variables.

numero_1 = 3
numero_2 = 7
numero_3 = 9

nombre = "Erick"
apellido = "Bailey"

# Operador SUMA
suma = numero_1 + numero_2
print(suma)
sumar_texto = nombre + " " + apellido # concatenacion
print(sumar_texto)

# Operador RESTA
resta = numero_1 - numero_2
print(resta)

# Operador MULTIPLICACIÓN
multiplicacion = numero_1 * numero_2
print(multiplicacion)
multiplicar_texto = nombre * numero_1
print(multiplicar_texto)
exponente = numero_1 ** numero_2 # Potencias
print(exponente)

# Operador DIVISIÓN
division = numero_3 / numero_1
print(division)
print(type(division))

division_baja = numero_3 // numero_2
print(division_baja)
print(type(division_baja))

# Mostrar con X cantidad de decimales
print(f"{numero_3 / numero_2:.4f}")

# Operador RESTO
op_resto = numero_3 % numero_2
print(op_resto)
